from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user
from .models import User, CommentList, Song


# Register your models here.
admin.site.register(User)
admin.site.register(CommentList)
admin.site.register(Song)
