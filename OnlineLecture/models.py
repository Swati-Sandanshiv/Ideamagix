from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

def validate_date(date):    
    if date < timezone.now().date():
        raise ValidationError("Data cannot be in the past")

class Instructors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    id = models.AutoField(primary_key=True)
    instructor = models.ForeignKey(Instructors, blank=True, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(validators=[validate_date])
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('instructor', 'date',)


