from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from students.models import  Student
from students.forms import  StudentForm, StudentModelForm

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


def students_index(request):
    students = Student.objects.all()
    return render(request,
                  'students/index.html',
              context={"students":students})

    # get all students from db

def student_show(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'students/show.html',
                  context={"student":student})



# def create_students(request):
#     ## request
#     print(request)
#     if request.method == 'POST':
#         print(request.POST) # to get data entered in the form
#         name = request.POST["name"]
#         age = request.POST["age"]
#         image = request.POST["image"]
#         email = request.POST['email']
#         student = Student()
#         student.name = name
#         student.age = age
#         student.email = email
#         student.image = image
#         student.save()
#
#         # return HttpResponse("object created")
#         # redirect to the index page
#         # return redirect("/students/index")
#         # reverse name to the url
#         url = reverse("students.index")
#         return redirect(url)
#
#         # students = Student.objects.all()
#         # return render(request,'students/students.html',
#         #               context={"students":students})
#
#
#
#     ## request GET
#     return render(request, 'students/create.html')
@login_required(login_url='/users/login')
def create_students(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST['email']
        student = Student()
        student.name = name
        if request.POST["age"]:
            student.age = request.POST['age']
        student.email = email
        try:
            student.image = request.FILES['image']
        except Exception as e:
            pass

        student.save()
        url = reverse("students.index")
        return redirect(url)

    # request GET
    return render(request, 'students/create.html')


def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    url = reverse("students.index")
    return redirect(url)


@login_required
def student_create_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = Student.create_object(request.POST['name'],
                                        request.POST['email'], request.POST['age'],
                                        request.FILES['image'])


            url = reverse("students.index")
            return redirect(url)


    return render(request, 'students/forms/create.html',
                  context={"form":form})



def student_create_model_form(request):
    form = StudentModelForm()

    if request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()  # return saved student
            # return HttpResponse(student.id)
            return redirect(student.show_url)

    return render(request, 'students/forms/create.html',
                  context={"form":form})


def edit_student(request, id):
    student = Student.get_student_by_id(id)
    form = StudentModelForm(instance=student) ## display old value in form fields
    if request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect(student.show_url)

    return render(request, 'students/forms/edit.html',
                  context={"form":form})


