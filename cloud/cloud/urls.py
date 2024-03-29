"""
URL configuration for cloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

from students.views import helloGhaza
from tracks.views import  tracks_home
from users.views import  profile
urlpatterns = [
    path('admin/', admin.site.urls),
    # path(url , viewfunction, name='urlname')
    path('ghaza', helloGhaza, name='hello_ghaza'),
    path("tracks/home", tracks_home , name='tracks_home'),
    # import url from other url_config files
    path('students/', include('students.urls')),
    path('tracks/', include('tracks.urls')),
    path('users/', include('users.urls')),
    path('accounts/profile/',profile,  )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
### I need to define the url of the media