# Generated by Django 3.1.4 on 2021-01-12 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineLecture', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OnlineLecture.course')),
                ('instructor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OnlineLecture.instructors')),
            ],
        ),
    ]
