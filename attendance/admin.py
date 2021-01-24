from django.contrib import admin
from .models import Subject, StudentRegisteredClass, Student

admin.site.register(StudentRegisteredClass)
admin.site.register(Subject)
admin.site.register(Student)
