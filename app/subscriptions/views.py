from django.core import signing
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, generics
from rest_framework.decorators import list_route
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from app.subscriptions.models import Mailing
from app.subscriptions.serializers import (
    CreateMailingSerializer,
    RetrieveMailingSerializer,
    CreateLettersStatusSerializer,
)


class MailingViewSet(viewsets.GenericViewSet):
    queryset = Mailing.objects.all()
    serializer_class = RetrieveMailingSerializer

    action_serializers = {
        'list': RetrieveMailingSerializer,
        'retrieve': RetrieveMailingSerializer,
        'create': CreateMailingSerializer
    }

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)

    def list(self, request, *args, **kwargs):
        from app.subscriptions.tasks import check_mailings
        check_mailings.delay()
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        mailings = get_object_or_404(self.get_queryset(), id=pk)
        response_data = self.get_serializer_class()(mailings).data
        return Response(response_data, status=status.HTTP_200_OK)

    def create(self, request):
        request_data = request.data.copy()
        serializer = self.get_serializer_class()(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @list_route(methods=['GET'])
    def open_tracking(self, request, *args, **kwargs):
        signed_key = request.query_params.get('k')

        try:
            user_id, mailing_id = signing.loads(signed_key)
        except Exception as err:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        instance = CreateLettersStatusSerializer(data={
            'user': user_id,
            'mailing': mailing_id,
            'has_been_read': True
        })
        instance.is_valid(raise_exception=True)
        instance.save()
        return Response(status=status.HTTP_201_CREATED)


class MailingsListView(generics.ListAPIView):
    queryset = Mailing.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        return Response(
            {'mailings': self.get_queryset()},
            template_name='pages/mailings.html'
        )
