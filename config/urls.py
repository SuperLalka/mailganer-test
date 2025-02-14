
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('api/', include('config.api_router')),
    url('', TemplateView.as_view(template_name='base.html'), name='home'),
]
