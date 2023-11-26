# views.py in your 'home' app

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'user': request.user})
    else:
        # Redirect to login or handle unauthorized access
        return render(request, 'home.html', {'user': None})