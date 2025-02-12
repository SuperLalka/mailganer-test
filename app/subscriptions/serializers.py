
from rest_framework import serializers

from app.subscriptions.models import Mailing


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = '__all__'


class RetrieveMailingSerializer(MailingSerializer):
    pass


class CreateMailingSerializer(MailingSerializer):
    pass
