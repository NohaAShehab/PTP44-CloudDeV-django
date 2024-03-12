from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# handle http request
def helloGhaza(request):  # request param --> represent http request
    # return "hello Ghaza"
    return HttpResponse("Hello Ghaza!")


def students_home(request):
    return HttpResponse("<h1> Hello from students page </h1>")


students = [
    {"id":1 , "name": "Nada", "image":"pic1.png"},
    {"id":2 , "name": "Mohamed", "image":"pic2.png"},
    {"id":3 , "name": "Nadin", "image":"pic3.png"},
    {"id":4 , "name": "Sara", "image":"pic4.png"}
]

def index(request):
    return HttpResponse(students)


# def profile(request , id ):
#     print(type(id))
#     for std in students:
#         if std['id']== id:
#             return HttpResponse(std.values())
#
#     return HttpResponse("Student not found")

def profile(request , id ):
    filtered_students = filter(lambda student: student["id"] == id, students)
    filtered_students = list(filtered_students)
    print(filtered_students)
    if filtered_students:
        # return HttpResponse(filtered_students[0].values())
        return render(request,
                      'students/profile.html',
                      context= {"student":filtered_students[0]})
    return HttpResponse("Student not found")


def landing(request):
    return render(request,
                  "students/landing.html",
                  context={"name": "noha", "students":students } )