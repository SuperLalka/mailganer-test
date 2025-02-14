from urllib import urlencode
from urlparse import urlunparse

from django.conf import settings
from django.core import signing


def get_open_tracking_url(user_id, mailing_id):
    q_params = urlencode({'k': signing.dumps((user_id, mailing_id))})
    return urlunparse([
        settings.MAIN_PROTOCOL,
        settings.MAIN_HOST,
        "/mailings/open_tracking/",
        '',
        q_params,
        ''
    ])
