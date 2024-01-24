from django.db import models
from main.models import BaseModel


class VideoCategory(BaseModel):
    name = models.CharField(max_length=255)

class Video(BaseModel):
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    type = models.CharField(max_length=255,null=True)
    file = models.FileField(upload_to='uploads/', null=True)

class Playlist(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class PlaylistVideo(BaseModel):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


    