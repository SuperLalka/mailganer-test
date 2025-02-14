import os

from celery import Celery
from django.conf import settings


if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


app = Celery("app")
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks()
