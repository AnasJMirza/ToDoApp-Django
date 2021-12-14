from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):

    form = UserCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'signup.html', context = context)
