from django.db import models

 
#collecting Spotify Auth information
class AuthInfo(models.Model):
    user_id = models.CharField(max_length=150, unique=True)
    #user = models.models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=250)
    refresh_token = models.CharField(max_length=250)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)
    
    def __str__(self):
        return (f'user: {self.user_id} // access_token: {self.access_token} // expires_in: {self.expires_in} \n\n')

