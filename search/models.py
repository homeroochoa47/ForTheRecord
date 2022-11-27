from django.db import models
 
#collecting Spotify Auth information
class AuthInfo(models.Model):
    session_id = models.CharField(max_length=50, unique=True) #TODO: Change this to user_id from spotify
    access_token = models.CharField(max_length=150)
    refresh_token = models.CharField(max_length=150)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)
    
    def __str__(self):
        return (f'user: {self.session_id} // access_token: {self.access_token} // expires_in: {self.expires_in} \n\n')

