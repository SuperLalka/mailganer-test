
from rest_framework import serializers

from app.subscriptions.models import LetterStatus, Mailing
from app.users.models import User


class LettersStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = LetterStatus
        fields = '__all__'


class RetrieveLettersStatusSerializer(LettersStatusSerializer):
    pass


class CreateLettersStatusSerializer(LettersStatusSerializer):
    mailing = serializers.PrimaryKeyRelatedField(queryset=Mailing.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
