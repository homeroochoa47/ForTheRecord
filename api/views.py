from django.shortcuts import render
from .serializers import SongSerializer, CommentListSerializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Song, CommentList


#TODO: add views to send serialized data to the frontend

#FIXME: figure out how this generic model works, otherwise just make them from scratch 
class CommentListView(generics.RetrieveAPIView, mixins.RetrieveModelMixin):
    serializer_class = CommentListSerializer
    
    def get_queryset(self,):
        user = self.request.user
        current_song = user.current_searched_song
        return CommentList.objects.filter(song=current_song.song_name)
    
    
class SongView(APIView):
    serializer_class = SongSerializer
    
    def get(self, request, format=None):
        current_song = request.user.current_searched_song
        data = SongSerializer(current_song).data
        return Response(data, status=status.HTTP_200_OK)