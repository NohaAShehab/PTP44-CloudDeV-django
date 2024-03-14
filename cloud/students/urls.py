

# add all urls_ related to students application

from django.urls import path
# import from students view

from students.views import (students_home, index,
    profile, landing, students_index,
                            student_show, create_students)

urlpatterns = [

    path('home', students_home, name='students.home' ),
    path('', index, name='students'),
    path('<int:id>', profile, name='students.profile'),
    path('land', landing, name='students.land'),
    path('index', students_index, name='students.index'),
    path('index/<int:id>', student_show, name='students.show'),
    path('create', create_students, name='students.create')

]