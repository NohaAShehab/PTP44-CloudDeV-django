# Generated by Django 5.0.3 on 2024-03-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_created_at_student_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='students/images/'),
        ),
    ]
