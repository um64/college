# views.py in your 'home' app

from django.shortcuts import render
from .models import UserProfile 

def home(request):
    return render(request, 'home.html')


def dashboard(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'dashboard.html', {'user': request.user, 'user_profile': user_profile})
        #return render(request, 'dashboard.html', {'user': request.user})
    else:
        # Redirect to login or handle unauthorized access
        return render(request, 'home.html', {'user': None})