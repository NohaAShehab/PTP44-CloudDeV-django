
from django import forms
from students.models import Student

class StudentForm(forms.Form):
    name = forms.CharField(label='Name' , max_length=100,
            help_text="Enter your name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',  max_length=100,
                        widget=forms.TextInput(attrs={'class': 'form-control'}) , help_text='Enter your email')
    age = forms.IntegerField( help_text="Enter your age", label="Age",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))


    # define validation rule for all fields
    def clean_email(self):
        email= self.cleaned_data['email']
        # check if email exists before ? return to page --> display form errors

        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")

        return email


    def clean_name(self):
        name= self.cleaned_data['name']
        if len(name) < 2:
             raise forms.ValidationError("Name must be at least 2 characters ")
        return name


## generate form based on the model
### model form ?

class StudentModelForm(forms.ModelForm):
    class Meta:
        model= Student
        fields = ['name', 'age', 'email', 'image']


    def clean_email(self):
        email= self.cleaned_data['email']
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")

        return email


    def clean_name(self):
        name= self.cleaned_data['name']
        if len(name) < 2:
             raise forms.ValidationError("Name must be at least 2 characters ")
        return name

    ## override save function
    # def save(self, commit=True):
    #     pass
