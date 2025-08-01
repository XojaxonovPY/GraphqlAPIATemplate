from rest_framework.fields import FileField
from rest_framework.serializers import Serializer, ModelSerializer

from apps.models import Media


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = 'image',

