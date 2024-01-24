from rest_framework import serializers
from rest_framework.fields import empty

from video.models import Video, VideoCategory, Playlist,PlaylistVideo



class VideoCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoCategory
        fields = (
            'name',
            )

class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = (
            'name', 'description'
            )

class VideoPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'category', 'name', 'description', 'type',
            )


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'id', 'category', 'name', 'description', 'type',
            'file',
            'user', 'date_created'

            )
        

class PlaylistVideoAddSerializer(serializers.ModelSerializer):
    action = serializers.CharField(read_only=True)
    # video = serializers.IntegerField(required=False)

    class Meta:
        model = PlaylistVideo
        fields = ('playlist', 'video', 'action')
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=PlaylistVideo.objects.all(),
        #         fields=['playlist', 'video']
        #     )
        # ]

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.fields['video'].required = False