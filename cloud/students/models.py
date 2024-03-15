from django.db import models
from django.shortcuts import  reverse, get_object_or_404
from tracks.models import Track


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, unique=True)
    image = models.ImageField(upload_to='students/images/',
                              null=True)

    age = models.IntegerField(default=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) # create
    updated_at = models.DateTimeField(auto_now=True, null=True)  # update
    track = models.ForeignKey(Track, on_delete=models.CASCADE,
                              null=True, related_name='students')  # track is an object from models
    # database --> add column track_id

    def __str__(self):
        return f"{self.name}"


    @property
    def image_url(self):
        return f'/media/{self.image}'

    @property
    def show_url(self):
        url = reverse('students.show', args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse('students.edit', args=[self.id])
        return url

    @classmethod
    def create_object(cls,name, email , age, image ):
        try:
            student = cls(name=name, email=email,image=image, age=age)
            print(name, email, age, image)
            student.save()
        except Exception as e:
            print(e)
            return False
        else:
            return student

    @classmethod
    def get_student_by_id(cls, id):
        return get_object_or_404(cls, id=id)


