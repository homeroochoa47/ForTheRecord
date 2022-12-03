from django.urls import path
from .views import SpotifyAuth, spotify_callback, get_current_track, check_spotify_auth, search_youtube_videos, retrieve_youtube_comments

urlpatterns = [
    path('', check_spotify_auth),
    path('check_for_auth',check_spotify_auth, name='check_auth'),
    path('spotify_auth', SpotifyAuth.as_view()),
    path('redirect', spotify_callback, name='callback'),
    path('spotify_search', get_current_track, name='spotify_search'),
    path('youtube_id_search', search_youtube_videos, name='youtube_id_search'),
    path('comment_search', retrieve_youtube_comments, name='comment_search')
]
