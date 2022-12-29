from rest_framework import serializers
from .models import User, Song, CommentList

#serializes the song object
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('song_name', 'artists', 'image_url', 'album_name', 'album_release_date', 'song_artist_info')

#calls the song serializer to serialize the song foreign key for this model. Then the serialized song object is passed on through along with the comments.
class CommentListSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)
    
    class Meta:
        model = CommentList
        fields = ('new_comments','song')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','current_searched_song', 'last_searched_song')
