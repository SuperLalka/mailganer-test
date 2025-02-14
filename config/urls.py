
from django.conf.urls import include, url
from django.contrib import admin

from app.subscriptions.views import MailingsListView
from app.users.views import HomePageView, UsersListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('api/', include('config.api_router')),

    url('page/mailings', MailingsListView.as_view(), name='mailings_page'),
    url('page/users', UsersListView.as_view(), name='users_page'),
    url('', HomePageView.as_view(), name='home'),
]
