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

    monday1 = models.CharField(max_length=10)
    monday2 = models.CharField(max_length=10)
    monday3 = models.CharField(max_length=10)
    monday4 = models.CharField(max_length=10)
    monday5 = models.CharField(max_length=10)

    tuesday1 = models.CharField(max_length=10)
    tuesday2 = models.CharField(max_length=10)
    tuesday3 = models.CharField(max_length=10)
    tuesday4 = models.CharField(max_length=10)
    tuesday5 = models.CharField(max_length=10)

    wednesday1 = models.CharField(max_length=10)
    wednesday2 = models.CharField(max_length=10)
    wednesday3 = models.CharField(max_length=10)
    wednesday4 = models.CharField(max_length=10)
    wednesday5 = models.CharField(max_length=10)

    thursday1 = models.CharField(max_length=10)
    thursday2 = models.CharField(max_length=10)
    thursday3 = models.CharField(max_length=10)
    thursday4 = models.CharField(max_length=10)
    thursday5 = models.CharField(max_length=10)

    friday1 = models.CharField(max_length=10)
    friday2 = models.CharField(max_length=10)
    friday3 = models.CharField(max_length=10)
    friday4 = models.CharField(max_length=10)
    friday5 = models.CharField(max_length=10)

    saturday1 = models.CharField(max_length=10)
    saturday2 = models.CharField(max_length=10)
    saturday3 = models.CharField(max_length=10)
    saturday4 = models.CharField(max_length=10)
    saturday5 = models.CharField(max_length=10)

    sunday1 = models.CharField(max_length=10)
    sunday2 = models.CharField(max_length=10)
    sunday3 = models.CharField(max_length=10)
    sunday4 = models.CharField(max_length=10)
    sunday5 = models.CharField(max_length=10)

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        s = Student(user=instance, points=100)
        s.save()
