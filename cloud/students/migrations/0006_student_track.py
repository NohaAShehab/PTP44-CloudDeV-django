# Generated by Django 5.0.3 on 2024-03-15 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_image'),
        ('tracks', '0002_track_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracks.track'),
        ),
    ]
