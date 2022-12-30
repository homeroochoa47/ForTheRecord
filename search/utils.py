from .models import AuthInfo
from api.models import User
from django.utils import timezone
from datetime import timedelta
from requests import post
import os
from requests import post, get

def get_user_auth_data(user_id):
    user_data = AuthInfo.objects.filter(user_id=user_id)
    
    if user_data.exists():
        return user_data[0]
    else:
        return None
    
def get_user_from_api_model(user_id):
    user_query = User.objects.filter(username=user_id)
    
    if user_query.exists():
        return user_query[0]
    else:
        return None

def create_or_update_auth_info(user_id, access_token, expires_in, refresh_token, token_type):
    
    #converts expires_in from seconds (3600 usually) to the actual time the token will expire at
    if type(expires_in) == int:
        expire_time = timezone.now() + timedelta(seconds=expires_in)
    else:
       expire_time = expires_in
    
    user_object = get_user_from_api_model(user_id)
    user_data = get_user_auth_data(user_id)
    
    #make a new model instance if theres no data for the specific session id
    if not user_data:
        auth_data_instance = AuthInfo(
            user_id = user_id,
            access_token = access_token,
            refresh_token = refresh_token, 
            expires_in = expire_time,
            token_type = token_type
        )
        auth_data_instance.save()
        user_object.update_auth_info(auth_data_instance)
        print(f'created new auth_info relation for {user_id}')
        
    #otherwise update the previous values from this session with the new ones
    else:
        user_data.access_token = access_token
        user_data.expires_in = expire_time
        user_data.token_type = token_type
        user_data.save(update_fields=['access_token', 'expires_in', 'token_type'])
        new_auth_info = AuthInfo.objects.get(user_id=user_id)
        user_object.update_auth_info(new_auth_info)
        print(f'updated previous auth_info object for {user_id}')
        
def check_or_update_spotify_token_status(user_id):
    #checks if the spotify token is expired, requests a new token if it is.
    user_data = get_user_auth_data(user_id)
    if user_data:
        if user_data.expires_in < timezone.now():
            refresh_spotify_token(user_id)
            'refreshed spotify auth_token'
            return
    print('\nspotify auth token still valid')

def refresh_spotify_token(user_id):
    refresh_token = get_user_auth_data(user_id).refresh_token

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': os.environ['CLIENT_ID'],
        'client_secret': os.environ['CLIENT_SECRET'],
    }).json()
    
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    
    create_or_update_auth_info(user_id, access_token, expires_in, refresh_token, token_type)
    
def retrieve_sporify_user_data(auth_token):
    user_info = get('https://api.spotify.com/v1/me',
                headers={
                    "authorization": f"Bearer {auth_token}" 
                }).json()
    return user_info.get("id")
    
    
def retrieve_comment_info_from_json(i, response):
    comment = response['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal']
    user = response['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName']
    user_profile_image = response['items'][i]['snippet']['topLevelComment']['snippet']['authorProfileImageUrl']
    
    if len(comment) < 750:
        return {'user': user, 'comment': comment, 'image': user_profile_image}