from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# handle http request
def helloGhaza(request):  # request param --> represent http request
    # return "hello Ghaza"
    return HttpResponse("Hello Ghaza!")


def students_home(request):
    return HttpResponse("<h1> Hello from students page </h1>")