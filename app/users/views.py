from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from app.users.models import User


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        return Response(
            {'users': self.get_queryset()},
            template_name='pages/users.html'
        )
