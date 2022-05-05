from rest_framework.serializers import ModelSerializer
from .models import ContentModel


class ContentSerializer(ModelSerializer):
    class Meta:
        model = ContentModel
        fields = '__all__'
