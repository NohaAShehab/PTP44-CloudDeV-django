from django.apps import AppConfig

# this file contains config class of the application
class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'  # name of the application
