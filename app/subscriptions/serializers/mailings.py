import datetime

from rest_framework import serializers

from app.subscriptions.models import Mailing


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = '__all__'


class RetrieveMailingSerializer(MailingSerializer):
    pass


class CreateMailingSerializer(MailingSerializer):
    sending_time = serializers.SerializerMethodField()

    def get_sending_time(self, obj):
        if self.initial_data.get('sending_time'):
            return datetime.datetime.fromtimestamp(self.initial_data['sending_time'])
