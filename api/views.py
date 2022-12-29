from django.shortcuts import render
from .serializers import SongSerializer, CommentListSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import User, Song, CommentList
from django.contrib.auth import get_user_model



#TODO: add views to send serialized data to the frontend
    
class CommentListView(APIView):
    serializer_class = CommentListSerializer
    
    def get(self, request, format=None):
        current_song = request.user.current_searched_song
        comment_list = CommentList.objects.filter(song=current_song)
        #print(f'\n\n\n COMMENT LIST HERE {comment_list} \n\n\n')
        #the data is returned as an object with the comments and the song data
        data = CommentListSerializer(comment_list[0]).data
        #print(data)
        return Response(data, status=status.HTTP_200_OK)
    
class SongView(APIView):
    serializer_class = SongSerializer
    lookup_url_kwarg = 'user'
    
    def get(self, request, format=None):
        current_song = request.user.current_searched_song
        data = SongSerializer(current_song).data
        return Response(data, status=status.HTTP_200_OK)
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'