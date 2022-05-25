from rest_framework import serializers
from Videos.models import Video

class VideoTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'created_at', 'video', 'get_transmission']


class VideoReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'created_at', 'video', 'get_reflection']


class VideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'video', 'video_ref', 'video_trans', 'video_stab']

    # def create(self, validated_data):
    #     name = validated_data.pop('name')
    #     roles = validated_data.pop('roles')
    #     customer = Customer.objects.create(name=name, **validated_data)
    #     _resolve_roles(customer, roles)
    #     customer.save()
    #     return customer
