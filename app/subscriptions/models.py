from __future__ import unicode_literals

from django.db import models
from tinymce import models as tinymce_models

from app.users.models import User


class Mailing(models.Model):
    title = models.CharField(max_length=128)
    sending_time = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    template = tinymce_models.HTMLField(blank=True, null=True)

    users = models.ManyToManyField(User, related_name='mailings', blank=True)


class LettersStatus(models.Model):
    has_been_read = models.BooleanField(default=False)
    reading_time = models.DateTimeField(auto_now_add=True)

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='letters_status')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='letters_status')
