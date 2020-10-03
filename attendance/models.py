from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    week = models.CharField(max_length=10)
    period = models.CharField(max_length=10)

class StudentTimetable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    week = models.CharField(max_length=10)
    period = models.CharField(max_length=10)
    subject = models.CharField(max_length=30, blank=True)

class StudentPoints(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=5)

@receiver(post_save, sender=User)
def create_student_data(sender, instance, created, **kwargs):
    if created:
        weeks = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
        periods = ['period1', 'period2', 
                    'period3', 'period4', 'period5']
        for week in weeks:
            for period in periods:
                record = StudentTimetable(user=instance, week=week, period=period)
                record.save()
        record = StudentPoints(user=instance, points=5)
        record.save()
