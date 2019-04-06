from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserRegistraterForm

def profile(request):
    return render(request, 'users/profile.html')