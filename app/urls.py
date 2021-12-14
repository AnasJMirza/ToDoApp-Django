
from django.contrib import admin
from django.http.response import HttpResponseNotAllowed
from django.urls import path
from app.views import home, login, signup





urlpatterns = [
    path("", home),
    path('login/', login),
    path('signup/', signup)
]
