
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from app.subscriptions.models import Mailing
from app.subscriptions.serializers import RetrieveMailingSerializer, CreateMailingSerializer


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
