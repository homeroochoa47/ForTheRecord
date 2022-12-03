from django.urls import path
from .views import CommentListView, SongView

urlpatterns = [
    path('comments', CommentListView.as_view()),
    path('song', SongView.as_view()),
]