

from django import  forms
from tracks.models import Track
class TrackForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    logo = forms.ImageField(required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        if Track.objects.filter(name=name).exists():
            raise forms.ValidationError("Name already taken before")
        return name
