from operator import is_
from telnetlib import STATUS
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from app.forms import TODOForm
from app.models import TODO

# Create your views here.

@login_required(login_url='login') # this will check if you are logged in or not
def home(request):
    
    #  getting the data from todos to show on this home page
    # todos = TODO.objects.all()  This will return all data without checking who is loged in

    # This will only show the data of the user who loged in

    if request.user.is_authenticated:
        user  = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')

        return render(request, 'index.html', context= {'form' : form, 'todos' : todos})

def login(request):

    if request.method == "GET":
        form = AuthenticationForm();

        context = {
            "form" : form
        }

        return render(request, 'login.html', context = context)

    else:
        form = AuthenticationForm(data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:
                loginUser(request, user)
                return redirect('home')
                

        else:
            context = {
                "form" : form
            }

            return render(request, 'login.html', context = context)



def delete_todo(request, id):
    TODO.objects.get(pk = id).delete() # gets the id of the item to be deleted

    # because after deleting we will show home page again

    return redirect('home')

# this function will cahnge the status of the todo
def change_todo(request, id, status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    # because after deleting we will show home page again
    return redirect('home')

def signup(request):

    if request.method == "GET" :
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request, 'signup.html', context = context)

    else :
        form = UserCreationForm(request.POST)
        context = {
            "form" : form
        }

        if form.is_valid():
            user = form.save()
            
            if user is not None:
                return redirect('login')
        else:

            return render(request, 'signup.html', context = context)

#  add todos in database
@login_required(login_url='login') # this will check if you are logged in or not
def add_todo(request):

    # Checking if the user is authenticate / loged in

    if request.user.is_authenticated:
        user  = request.user
        print(user)

    # Saving / adding data into database

        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            # returning the same page showing the errors
            return render(request, 'index.html', context= {'form' : form})
         


#  signout funtion for user to signout

def signout(request):
    logout(request);
    return redirect('login')