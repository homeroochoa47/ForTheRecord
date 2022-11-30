from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import UserManager
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

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    auth_info = models.ForeignKey(AuthInfo, on_delete=models.CASCADE, default=None, null=True)
    last_searched_song = models.ForeignKey(Song, on_delete=models.CASCADE, default=None, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True,)
    date_joined = models.DateTimeField(default=timezone.now)
    
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
    
    def update_auth_info(self, auth_info_object):
        self.auth_info = auth_info_object
        self.save(update_fields=['auth_info'])
        
    def update_last_searched_song(self, last_song_object):
        self.last_searched_song = last_song_object
        self.save(update_fields=['last_searched_song'])