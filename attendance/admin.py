from django.contrib import admin
from .models import Subject, Student

admin.site.register(Student)
admin.site.register(Subject)