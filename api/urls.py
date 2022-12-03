from django.urls import path, include
from .views import CommentListView, SongView, UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('comments', CommentListView.as_view()),
    path('song', SongView.as_view()),
    path('', include(router.urls)),
]