from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from app.users.models import User


class HomePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        kwargs['users'] = User.objects.all()
        return super(HomePageView, self).get_context_data(**kwargs)


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        return Response(
            {'users': self.get_queryset()},
            template_name='pages/users.html'
        )
