from json import JSONDecodeError, dumps
from django.shortcuts import render, redirect
from requests import Request, post, get
from .creds import REDIRECT_URI, CLIENT_ID, CLIENT_SECRET, youtube_api_key, api_service_name, api_version
from .utils import create_or_update_auth_info, check_spotify_authentication, get_user_auth_data, retrieve_comment_info_from_json, retrieve_sporify_user_data, get_user_from_api_model
import html
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from api.models import User, Song

#for youtube API
import os
import googleapiclient.discovery
import googleapiclient.errors

#TODO: Update views here to add data to appropriate models.
#TODO: Figure out if we're going to have separate functionality depending on whether or not a user is logged in

class SpotifyAuth(APIView):
    
    def get(self, request, format=None):
        scopes = ('user-read-currently-playing', 'user-read-private')
        
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI ,
            'client_id': CLIENT_ID
        }).prepare().url
        
        return Response({'url': url}, status=status.HTTP_200_OK)
    

def spotify_callback(request):
    #TODO: We might need to remake this to avoid just getting a new auth token every time, and instead have it check if theres one present/if its expired and go from there
    code = request.GET.get('code')
    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()
                                                         
    #storing data from the json above
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    refresh_token = response.get('refresh_token')
    
    spotify_user_id = retrieve_sporify_user_data(access_token)
    
    #TODO: Condense this whole section into an authenticate and login util function, dont forget to make the session
    
    if not request.session.exists(request.session.session_key): #if there is no session
        request.session.create() #make a session
    
    user = authenticate(
        request=request,
        username=spotify_user_id
    )
    
    if user is not None:
        login(request, user)
    else:
        print('Something went wrong')
    
    #update the data associated to the session key
    create_or_update_auth_info(request.user, access_token, expires_in, refresh_token, token_type)
    print (User.objects.get(username=spotify_user_id).auth_info)
    
    return redirect('/search/spotify_search')

#calls the spotify api for the users currently playing song
def get_current_track(request):
    user_object = get_user_from_api_model(request.user)
    user_auth_token = user_object.auth_info.access_token
    
    try:
        track_info = get('https://api.spotify.com/v1/me/player/currently-playing?market=us',
                headers={
                    "authorization": f"Bearer {user_auth_token}" 
                }).json()
    except JSONDecodeError: #this is the error we get if the music on spotify is paused/nothing is playing
        return render(request, 'JSONDecodeError/JSONDecodeError.html')
        #TODO: change this to a Rest Framework error message instead
    
    #filtering through the json dict for the info we want
    #we might be able to do this more efficiently with the get() function
    track_name = track_info['item']['name']
    artists = track_info['item']['artists']
    artist_names = ', '.join([artist['name'] for artist in artists])
    image_url = track_info['item']['album']['images'][1]['url']
    album_name = track_info['item']['album']['name']
    album_release_date = track_info['item']['album']['release_date']
    song_artist_info = (f'{track_name} {artist_names}')

    searched_song = Song(
        song_name = track_name,
        artists = artist_names,
        image_url = image_url,
        album_name = album_name,
        album_release_date = album_release_date[0:4],
        song_artist_info = song_artist_info
        )
    
    searched_song.save()
    #TODO: Not sure if we wanna accumulate the searched songs in the database every time. Find some good database maintainance practices for this.
    
    user_object.update_last_searched_song(searched_song)
    print(f'\n\nSONG HERE {user_object.last_searched_song}\n\n')
    
    request.session['song_info'] = {
        'song_artist_info': song_artist_info,
        'artists': artist_names, 'track': track_name,
        'album': album_name,
        'cover_url': image_url,
        'album_release_date': album_release_date[0:4]}
    
    return redirect('youtube_id_search')

#check if there is a valid auth token for the access token. if there is, skip the auth process and go directly to get_current_track. If there isnt, get a new auth token.
def check_spotify_auth(request):
    try:
        session = request.session.session_key
        
    except:
        return redirect('/search/spotify_auth')
    
    authenticated = check_spotify_authentication(session) #returns a bool
    if authenticated == True:
        return redirect('/search/spotify_search')
    else:
        return redirect('/search/spotify_auth')

    
#Using the song information from the spotify track to search for video ID's for that song on youtube.
def search_youtube_videos(request):
    track_to_search = request.session['song_info']['song_artist_info']
       
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    #taken from the youtube data api
    youtube = googleapiclient.discovery.build(
        api_service_name,
        api_version, 
        developerKey = youtube_api_key
    )
    
    req = youtube.search().list(
        part="snippet",
        maxResults=3,
        order="relevance",
        q=track_to_search,
        topicId="/m/04rlf",
        type='video'
    )
    response = req.execute()
    video_ids = {}
    
    #pulls the video id from the json dict for 3 videos
    for i in range(3):
        video_name = response["items"][i]['snippet']['title']
        video_id = response["items"][i]['id']['videoId']
        video_ids[video_id] = video_name
        
    request.session['video_ids'] = video_ids
    
    return redirect('/search/comment_search')

#make this an APIView that sends back the json file with the comments and song info to the front end instead of saving it in the session instead of passing the data as context
#this will either involve 
def retrieve_youtube_comments(request):
    video_ids = request.session['video_ids']
    print (f'\n\nVIDEO IDS: {video_ids}\n\n')
    comments = [] #maybe change to user data, list of dicts with user id, comment
    
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    
    youtube = googleapiclient.discovery.build(
        api_service_name, 
        api_version, 
        developerKey = youtube_api_key
    )
    
    #for each of the three video ids, get the comments
    for video_id in video_ids.keys():
        video_name = video_ids[video_id]
        print (f'SONG NAME: {html.unescape((video_name))}\n\n') #prints decoded string
        
        req = youtube.commentThreads().list(
            part="snippet",
            maxResults=20,
            order="relevance",
            videoId=video_id
        )
        try:
            response = req.execute()
        except googleapiclient.errors.HttpError:
            continue

        #checking the number of comments, allowing 20 max
        number_of_comments = len(response['items'])
        
        if number_of_comments == 0:
            continue

        for x in range(number_of_comments):
            comment_data = retrieve_comment_info_from_json(x, response)
            if comment_data is not None:
                comments.append(comment_data)
    #if there werent any comments found
    if len(comments) == 0:
        comments = [{'comment': "Sorry, looks like we werent able to find any comments"}]
        #alternatively, return a new render with a separate html file for a new page reading the message we want.
    
    #this will be used to save the comments in the api CommentList model as a json
    comments_json = dumps(comments)
    
    context = {
        'yt_comments': comments,
        'track_name': request.session['song_info']['track'],
        'artists': request.session['song_info']['artists'],
        'album': request.session['song_info']['album'],
        'cover_url': request.session['song_info']['cover_url'],
        'release_date': request.session['song_info']['album_release_date']
    }
    
    return render(request, 'comments/comments.html', context)