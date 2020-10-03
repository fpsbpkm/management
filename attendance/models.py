from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Subject(models.Model):
    subject_name = models.CharField(max_length=10)
    # 月曜日から日曜日まで順に1~7を割り当て
    week = models.IntegerField()
    time = models.IntegerField()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    monday1 = models.CharField(max_length=10, blank=True)
    monday2 = models.CharField(max_length=10, blank=True)
    monday3 = models.CharField(max_length=10, blank=True)
    monday4 = models.CharField(max_length=10, blank=True)
    monday5 = models.CharField(max_length=10, blank=True)

    tuesday1 = models.CharField(max_length=10, blank=True)
    tuesday2 = models.CharField(max_length=10, blank=True)
    tuesday3 = models.CharField(max_length=10, blank=True)
    tuesday4 = models.CharField(max_length=10, blank=True)
    tuesday5 = models.CharField(max_length=10, blank=True)

    wednesday1 = models.CharField(max_length=10, blank=True)
    wednesday2 = models.CharField(max_length=10, blank=True)
    wednesday3 = models.CharField(max_length=10, blank=True)
    wednesday4 = models.CharField(max_length=10, blank=True)
    wednesday5 = models.CharField(max_length=10, blank=True)

    thursday1 = models.CharField(max_length=10, blank=True)
    thursday2 = models.CharField(max_length=10, blank=True)
    thursday3 = models.CharField(max_length=10, blank=True)
    thursday4 = models.CharField(max_length=10, blank=True)
    thursday5 = models.CharField(max_length=10, blank=True)

    friday1 = models.CharField(max_length=10, blank=True)
    friday2 = models.CharField(max_length=10, blank=True)
    friday3 = models.CharField(max_length=10, blank=True)
    friday4 = models.CharField(max_length=10, blank=True)
    friday5 = models.CharField(max_length=10, blank=True)

    saturday1 = models.CharField(max_length=10, blank=True)
    saturday2 = models.CharField(max_length=10, blank=True)
    saturday3 = models.CharField(max_length=10, blank=True)
    saturday4 = models.CharField(max_length=10, blank=True)
    saturday5 = models.CharField(max_length=10, blank=True)

    sunday1 = models.CharField(max_length=10, blank=True)
    sunday2 = models.CharField(max_length=10, blank=True)
    sunday3 = models.CharField(max_length=10, blank=True)
    sunday4 = models.CharField(max_length=10, blank=True)
    sunday5 = models.CharField(max_length=10, blank=True)

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        s = Student(user=instance, points=100)
        s.save()
