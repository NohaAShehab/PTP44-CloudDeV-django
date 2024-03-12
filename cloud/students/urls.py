

# add all urls_ related to students application

from django.urls import path
# import from students view

from students.views import students_home, index, profile, landing

urlpatterns = [

    path('home', students_home, name='students.home' ),
    path('', index, name='students.index'),
    path('<int:id>', profile, name='students.profile'),
    path('land', landing, name='students.land')

]