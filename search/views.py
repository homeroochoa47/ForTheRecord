from json import JSONDecodeError, dumps
from django.shortcuts import render, redirect
from requests import Request, post, get
from .utils import create_or_update_auth_info, check_or_update_spotify_token_status, get_user_auth_data, retrieve_comment_info_from_json, retrieve_sporify_user_data, get_user_from_api_model
import html
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from api.models import User, Song, CommentList

#for youtube API
import os
import googleapiclient.discovery
import googleapiclient.errors
import json

#TODO: Figure out if we're going to have separate functionality depending on whether or not a user is logged in

class SpotifyAuth(APIView):
    
    def get(self, request, format=None):
        scopes = ('user-read-currently-playing', 'user-read-private')
        
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': os.environ['REDIRECT_URI'],
            'client_id': os.environ['CLIENT_ID']
        }).prepare().url
        
        return Response({'spotify_auth_url': url}, status=status.HTTP_200_OK)
    

def spotify_callback(request):
    #TODO: We might need to remake this to avoid just getting a new auth token every time, and instead have it check if theres one present/if its expired and go from there
    code = request.GET.get('code')
    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': os.environ['REDIRECT_URI'],
        'client_id': os.environ['CLIENT_ID'],
        'client_secret': os.environ['CLIENT_SECRET']
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
    
    return redirect('/comments') #authenticates and then redirects back to the frontend

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
    
    user_object.update_user_saved_songs(searched_song)
    print(f'\n\nSONG HERE {user_object.current_searched_song}\n\n')
    
    return redirect('youtube_id_search')

#check if there is a valid auth token for the access token. if there is, skip the auth process and go directly to get_current_track. If there isnt, get a new auth token.
def check_spotify_auth(request):
    if request.user.is_authenticated:
        check_or_update_spotify_token_status(request.user)
        print('user is authenticated, sending to search\n')
        return redirect('/search/spotify_search')
    else:
        print('user not authenticated, sending to auth\n')
        #if we were to allow for functionality for anonymous users, this would be where we fork them elsewhere.
        return redirect('/search/spotify_auth')

    
#Using the song information from the spotify track to search for video ID's for that song on youtube.
def search_youtube_videos(request):
    track_to_search = request.user.current_searched_song.song_artist_info
       
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    #taken from the youtube data api
    youtube = googleapiclient.discovery.build(
        os.environ['api_service_name'],
        os.environ['api_version'], 
        developerKey = os.environ['youtube_api_key']
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

@api_view(['GET', 'POST'])
def retrieve_youtube_comments(request):
    current_song = request.user.current_searched_song
    video_ids = request.session['video_ids'] #TODO: maybe save this to the Song model?
    print (f'\n\nVIDEO IDS: {video_ids}\n\n')
    comments = []
    
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    
    youtube = googleapiclient.discovery.build(
        os.environ['api_service_name'], 
        os.environ['api_version'], 
        developerKey = os.environ['youtube_api_key']
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
            continue #move on to the next video

        #checking the number of comments, allowing 20 max per the request to the youtube api above: 'maxResults=20'
        number_of_comments = len(response['items'])
        if number_of_comments == 0:
            continue #move on to the next video if there were no comments

        for i in range(number_of_comments):
            comment_data = retrieve_comment_info_from_json(i, response) #returns the comment, youtube username, and profile image; will = None if comment is too long
            if comment_data is not None:
                comments.append(comment_data)
    #if there werent any comments found
    if len(comments) == 0:
        comments = [{'comment': "Sorry, looks like we werent able to find any comments"}]
        #alternatively, return a new render with a separate html file for a new page reading the message we want.
    
    #first sorting the comments in descending order of length for easier presentation on the fron end.
    comments = sorted(comments, key=lambda x: len(x['comment']), reverse=True)
    
    comment_list = CommentList(new_comments=comments, song=current_song)
    comment_list.save()
    
    return redirect('/api/comments')
    #return Response(comment_list.comments)