from django.db import models
from django.contrib.auth.models import AbstractUser
from search.models import AuthInfo

#TODO: update models to allow for user to save comments that they like

class CommentList(models.Model):
    #have the comments saved here in a json with the username of the commenter
    comment_list = models.TextField()

class Song(models.Model):
    song_name = models.CharField(max_length=100)
    artists = models.CharField(max_length=150)
    image_url = models.URLField()
    album_name = models.CharField(max_length=75)
    album_release_date = models.IntegerField()
    song_artist_info = models.CharField(max_length=100)
    comments = models.ForeignKey(CommentList, on_delete=models.CASCADE)


class User(AbstractUser):
    username = models.CharField(max_length=50)
    is_staff=models.BooleanField(default=False)
    auth_info = models.ForeignKey(AuthInfo, on_delete=models.CASCADE)
    last_searched_song = models.ForeignKey(Song, on_delete=models.CASCADE)