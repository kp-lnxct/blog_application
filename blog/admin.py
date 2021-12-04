from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class user_admin(admin.ModelAdmin):
    list_display = ['title', 'date']


@admin.register(Profile)
class admin_profile(admin.ModelAdmin):
    list_display = ['id','user_id','image']