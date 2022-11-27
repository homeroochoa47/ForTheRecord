from rest_framework import serializers
from .models import User, Song, CommentList

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentList
        fields = ('comment_list')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'auth_info', 'last_searched_song')
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('song_name', 'artists', 'image_url', 'album_name', 'album_release_date', 'song_artist_info', 'comments')