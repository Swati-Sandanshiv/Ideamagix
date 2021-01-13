from django.contrib import admin
from . models import Instructors,Course,Lecture

# Register your models here.
admin.site.site_header = "Lecture Schedule - Login"
admin.site.site_title = "Online Lecture Scheduling Module"
admin.site.index_title = "Welcome to the Online Lecture Scheduling Module"


class InstructorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','status')
admin.site.register(Instructors, InstructorsAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level','status')
admin.site.register(Course, CourseAdmin)

class LectureAdmin(admin.ModelAdmin):
    list_display = ('instructor','course', 'date','status')
admin.site.register(Lecture, LectureAdmin)

