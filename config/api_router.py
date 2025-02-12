from rest_framework.routers import DefaultRouter

from app.subscriptions.views import MailingViewSet

router = DefaultRouter()

router.register('mailings', MailingViewSet, base_name='mailings')
# router.register('users', UserViewSet, base_name='users')

app_name = 'api'
urlpatterns = router.urls
