

from django.urls import path
from tracks.views import  tracks_landing
urlpatterns = [

    path('landing',tracks_landing, name='tracks.landing' )

]