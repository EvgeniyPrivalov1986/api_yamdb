from django.shortcuts import render
from .models import User

def profile(request):
    users = User.objects.all()
    return render(request, 'reviews/profile.html', {'users': users})
