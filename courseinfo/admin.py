from django.contrib import admin
from .models import Year, Course, Period, Instructor, Student, Registration, Section, Semester
# Register your models here.
admin.site.register(Period)
admin.site.register(Year)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(Section)
admin.site.register(Semester)
