from django.db import models

# Create your models here.

class Student(models.Model):
    # when create field in model ---> its default --> not null
    # unless you say it accepts null explicitly
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, unique=True)
    image = models.CharField(max_length=100, null=True)
    age = models.IntegerField(default=10, null=True)
    ## reflect when has been created and when has been modified
    created_at = models.DateTimeField(auto_now_add=True, null=True) # create
    updated_at = models.DateTimeField(auto_now=True, null=True)  # update

    def __str__(self):
        return f"{self.name}"

