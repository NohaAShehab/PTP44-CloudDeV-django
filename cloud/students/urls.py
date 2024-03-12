

# add all urls_ related to students application

from django.urls import path
# import from students view

from students.views import students_home

urlpatterns = [

    path('home', students_home, name='students.home' )
]