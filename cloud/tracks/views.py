from django.shortcuts import render
from django.http import  HttpResponse

from tracks.models import Track
from tracks.forms import TrackForm

# Create your views here.


def tracks_home(request):
    return HttpResponse("<h1>Welcome to tracks home page </h1>")


def tracks_landing(request):
    return render(request, "tracks/landing.html")

## list all , create , update , delete


## create form to add new track

def create_track(request):
    form = TrackForm()
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES )
        if form.is_valid():
            track = Track(name=form.cleaned_data['name'],
                          description=form.cleaned_data['description'],
                          logo=form.cleaned_data['logo'])
            track.save()
            return HttpResponse("Track added successfully")

    return render(request,
    "tracks/create.html",
                  context={'form': form})


def tracks_index(request):
    tracks = Track.get_all_tracks()
    return render(request, "tracks/index.html",
                  context={"tracks": tracks})


def show_track(request, id):
    track = Track.get_sepcific_track(id)
    return render(request, "tracks/show.html",
                  context={"track": track})

