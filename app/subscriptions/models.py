from __future__ import unicode_literals

from django.db import models

from app.users.models import User


class Mailing(models.Model):
    title = models.CharField(max_length=128)
    sending_time = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    content = models.TextField()

    template = models.ForeignKey('MailTemplate', on_delete=models.PROTECT, related_name='mailings', null=True)
    users = models.ManyToManyField(User, related_name='mailings', blank=True)

    class Meta:
        db_table = 'mailing'
        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'


class MailTemplate(models.Model):
    subject = models.CharField(max_length=128)
    html_data = models.TextField()
    text_data = models.TextField()

    class Meta:
        db_table = 'mail_template'
        verbose_name = 'MailTemplate'
        verbose_name_plural = 'MailTemplates'


class LetterStatus(models.Model):
    has_been_read = models.BooleanField(default=False)
    reading_time = models.DateTimeField(auto_now_add=True)

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='letters_status')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='letters_status')

    class Meta:
        db_table = 'letter_status'
        verbose_name = 'LetterStatus'
        verbose_name_plural = 'LettersStatus'
        unique_together = ['mailing', 'user']
