
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView

from app.subscriptions.views import MailingsListView
from app.users.views import UsersListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('api/', include('config.api_router')),

    url('page/mailings', MailingsListView.as_view(), name='mailings_page'),
    url('page/users', UsersListView.as_view(), name='users_page'),
    url('', TemplateView.as_view(template_name='base.html'), name='home'),
]
