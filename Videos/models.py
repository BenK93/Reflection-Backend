from django.db import models
from Users.models import User
from django.utils import timezone

from Videos.separation.extract_layers import get_layer
# Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='uploads/')
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    # video_reflection = models.FileField(upload_to='uploads/reflections/', blank=True)
    # video_transmission = models.FileField(upload_to='uploads/transmissions/', blank=True)

    @property
    def get_reflection(self):
        # return get_layer(self.video.name, 'reflection')
        return "reflection"

    @property
    def get_transmission(self):
        return get_layer(self.video.name, 'transmissions')

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.name
