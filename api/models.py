from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import UserManager
from search.models import AuthInfo

#TODO: update models to allow for user to save comments that they like

class Song(models.Model):
    song_name = models.CharField(max_length=250)
    artists = models.CharField(max_length=150)
    image_url = models.URLField()
    album_name = models.CharField(max_length=75)
    album_release_date = models.IntegerField()
    song_artist_info = models.CharField(max_length=300)
    
    def __str__(self):
        return (f'{self.song_name}, {self.artists}')

class CommentList(models.Model):
    #have the comments saved here in a json with the username of the commenter
    comments = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.comments

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    auth_info = models.ForeignKey(AuthInfo, on_delete=models.CASCADE, default=None, null=True)
    current_searched_song = models.ForeignKey(Song, on_delete=models.CASCADE, default=None, null=True, related_name='current_searched_song')
    last_searched_song = models.ForeignKey(Song, on_delete=models.CASCADE, default=None, null=True, related_name='last_searched_song')
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
        
    def update_user_saved_songs(self, new_searched_song):
        #if theres a last searched song, replace that with the current searched song and delete the now unused song model
        #then replace the current searched song with the song that is being passed through the funciton, which will be our new current
        if self.last_searched_song is not None:
            print ("Executed Case 1")
            song_object = self.last_searched_song
            print(f'Removing: {song_object}')
            self.last_searched_song = self.current_searched_song
            self.current_searched_song = new_searched_song
            self.save(update_fields=['last_searched_song', 'current_searched_song'])            
            song_object.delete()
            return
        #if this user does not have any saved songs, set the current searched song to the searched song. No last searched song until the next request
        elif self.current_searched_song is None and self.last_searched_song is None:
            print ("Executed Case 2")
            self.current_searched_song = new_searched_song
            self.save(update_fields=['current_searched_song'])
            return
        #if there is no last searched song, set that empty entry to the current searched song and move on
        elif self.last_searched_song is None:
            print ("Executed Case 3")
            self.last_searched_song = self.current_searched_song
            self.save(update_fields=['last_searched_song'])
            self.current_searched_song = new_searched_song
            self.save(update_fields=['last_searched_song', 'current_searched_song'])