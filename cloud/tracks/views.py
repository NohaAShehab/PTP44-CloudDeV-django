from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.


def tracks_home(request):
    return HttpResponse("<h1>Welcome to tracks home page </h1>")


## list all , create , update , delete