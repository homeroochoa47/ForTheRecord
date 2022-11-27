from django.contrib import admin
from .models import User, CommentList, Song

# Register your models here.
admin.site.register(User)
admin.site.register(CommentList)
admin.site.register(Song)