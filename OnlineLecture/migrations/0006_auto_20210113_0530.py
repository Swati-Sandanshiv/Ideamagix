# Generated by Django 3.1.4 on 2021-01-13 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineLecture', '0005_auto_20210113_0236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='instructor_id',
            new_name='instructor',
        ),
    ]
