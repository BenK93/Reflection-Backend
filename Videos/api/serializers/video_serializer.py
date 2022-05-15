from rest_framework.serializers import serializers
from Videos.models import Video

class VideoTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'created_at', 'video', 'user', 'get_transmission']


class VideoReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'created_at', 'video', 'user', 'get_reflection']


class VideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'video', 'user']