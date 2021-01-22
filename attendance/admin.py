from django.contrib import admin
from .models import Subject, StudentTimetable

admin.site.register(StudentTimetable)
admin.site.register(Subject)