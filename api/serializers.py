from rest_framework import serializers
from .models import User, Song, CommentList
from search.models import AuthInfo

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentList
        fields = ('comments','song')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','current_searched_song', 'last_searched_song')
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('song_name', 'artists', 'image_url', 'album_name', 'album_release_date', 'song_artist_info')
