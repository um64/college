# backend/urls.py

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', include('register.urls')),  
    path('login/', include('login.urls')),
    path('about/', include('about.urls')),
    
]
