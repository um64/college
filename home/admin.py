# Inside your_app_name/admin.py

from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)
