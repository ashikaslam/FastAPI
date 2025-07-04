# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'email','first_name','last_name','phone', 'profile_image']
    ordering = ['-id']

    
