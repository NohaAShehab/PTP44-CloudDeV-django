from django.db import models
from django.shortcuts import reverse, get_object_or_404
# Create your models here.


class Track(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    logo = models.ImageField(upload_to='tracks/logos/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"

    @property
    def logo_url(self) -> str:
        return f"/media/{self.logo}"

    @property
    def show_url(self) -> str:
        url = reverse("tracks.show", args=[self.id])
        return url


    @classmethod
    def get_all_tracks(cls):
        return cls.objects.all()

    @classmethod
    def get_sepcific_track(cls, id):
        # return cls.objects.get(id=id)
        return get_object_or_404(cls,id=id)










