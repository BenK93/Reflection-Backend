from threading import Thread
import copy
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers.video_serializer import VideoReflectionSerializer, VideoTransmissionSerializer, VideoCreateSerializer
from Videos.models import Video
from rest_framework import permissions, status, viewsets

from ..separation.extract_layers import get_all_layers


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        return VideoCreateSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        ref, trans, stab = get_all_layers(data['video'])
        data['video_ref'] = ref
        data['video_trans'] = trans
        data['video_stab'] = stab
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        """
            to not respond to http://127.0.0.1:8000/api/messages/
            so when there a lot of messages it can take time
        """
        return Response(status=status.HTTP_403_FORBIDDEN)
