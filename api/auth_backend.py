from .models import User 
from django.conf import settings

# requires to define two functions authenticate and get_user

class SpotifyAuthBackend:  

    def authenticate(self, request, username=None):
        print('\nauthenticating...')
        #we check if the user_id is already in the database and return that user if they are. If not we create a new user instance with that name.
        try:
            user = User.objects.get(username=username)
            print('found user')
            print (f'returning {user}')
        except User.DoesNotExist:
            user = User(username=username)
            user.save()
            print('made a new user')
            print (f'returning {user}')
        return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    