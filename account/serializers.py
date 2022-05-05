from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import UserModel


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
