from .models import AuthInfo
from django.utils import timezone
from datetime import timedelta
from requests import post
from .creds import CLIENT_ID, CLIENT_SECRET

def get_user_auth_data(session_id):
    user_data = AuthInfo.objects.filter(sessio=session_id)
    
    if user_data.exists():
        return user_data[0]
    else:
        return None

def create_or_update_auth_info(session_id, access_token, expires_in, refresh_token, token_type):
    
    #converts expires_in from seconds (3600 usually) to the actual time the token will expire at
    if type(expires_in) == int:
        expire_time = timezone.now() + timedelta(seconds=expires_in)
    else:
       expire_time = expires_in
       
    user_data = get_user_auth_data(session_id)
    
    #make a new model instance if theres no data for the specific session id
    if not user_data:
        auth_data_instance = AuthInfo(
            session_id = session_id,
            access_token = access_token,
            refresh_token = refresh_token, 
            expires_in = expire_time,
            token_type = token_type
        )
        auth_data_instance.save()
    #otherwise update the previous values from this session with the new ones
    else:
        user_data.access_token = access_token
        user_data.expires_in = expire_time
        user_data.token_type = token_type
        user_data.save(update_fields=['access_token', 'expires_in', 'token_type'])

        
def check_spotify_authentication(session_id):
    user_data = get_user_auth_data(session_id)
    
    if user_data:
        if user_data.expires_in < timezone.now():
            refresh_spotify_token(session_id)
            return True
    return False

#somethings wrong here, maybe in the response
def refresh_spotify_token(session_id):
    refresh_token = get_user_auth_data(session_id).refresh_token

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }).json()
    
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    
    create_or_update_auth_info(session_id, access_token, expires_in, refresh_token, token_type)
    
def save_searched_track(session_id, track):
    #we can use this function to save tracks to the song model in the api
    pass
    
    
    
def retrieve_comment_info_from_json(i, response):
    comment = response['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal']
    user = response['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName']
    user_profile_image = response['items'][i]['snippet']['topLevelComment']['snippet']['authorProfileImageUrl']
    
    if len(comment) < 750:
        return {'user': user, 'comment': comment, 'image': user_profile_image}