from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.


def tracks_home(request):
    return HttpResponse("<h1>Welcome to tracks home page </h1>")


def tracks_landing(request):
    return render(request, "tracks/landing.html")

## list all , create , update , delete