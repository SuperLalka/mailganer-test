import datetime

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.template import Context, Template
from django.template.loader import render_to_string

from app.subscriptions.models import Mailing
from app.utils.celery import CeleryHelper
from app.utils.utils import get_open_tracking_url
from config.celery_app import app

User = get_user_model()


@app.task
def check_mailings():
    for obj in Mailing.objects.filter(
        Q(is_completed=False),
        Q(sending_time__isnull=True) | Q(sending_time__lte=datetime.datetime.now())
    ):
        if not CeleryHelper.is_being_executed('start_mailings', obj.id):
            start_mailings.delay(obj.id)


@app.task
def start_mailings(mailing_id):
    mailing = (
        Mailing.objects.filter(id=mailing_id)
        .prefetch_related('users')
        .select_related('template')
        .first()
    )

    for recipient in mailing.users.all():
        send_mail.delay({
                'content': mailing.content,
                'subject': mailing.template.subject,
                'text_data': mailing.template.text_data,
                'html_data': mailing.template.html_data,
                'open_tracking_url': get_open_tracking_url(recipient.id, mailing.id)
        },
            {
                'user_username': recipient.username,
                'user_email': recipient.email,
            }
        )

    mailing.is_completed = True
    mailing.save(update_fields=['is_completed'])


@app.task
def send_mail(mail_data, user_data):
    context = dict()
    context.update(mail_data)
    context.update(user_data)

    subject_tmpl = Template(mail_data['subject'])
    subject_cont = Context(context)
    subject = subject_tmpl.render(subject_cont)

    text_content_tmpl = Template(mail_data['text_data'])
    text_content_cont = Context(context)
    text_content = text_content_tmpl.render(text_content_cont)

    html_content_tmpl = Template(mail_data['html_data'])
    html_content_cont = Context(context)
    context['html_data'] = html_content_tmpl.render(html_content_cont)
    html_content = render_to_string('mails/mail_base.html', context=context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        # from_email=...,
        to=[user_data['user_email']],
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()
