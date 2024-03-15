

from django.urls import path
from tracks.views import  tracks_landing, create_track, tracks_index, show_track

urlpatterns = [

    path('landing',tracks_landing, name='tracks.landing' ),
    path('create',create_track, name='tracks.create'),
    path('',tracks_index, name='tracks.index' ),
    path('<int:id>', show_track, name='tracks.show')

]