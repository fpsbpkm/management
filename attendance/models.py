from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    week = models.CharField(max_length=10)
    period = models.CharField(max_length=10)

class StudentRegisteredClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    week = models.CharField(max_length=10)
    period = models.CharField(max_length=10)
    subject = models.CharField(max_length=30, blank=True)

    def register_class(self, request):
        subject = request.POST['subject']
        week = request.POST['week']
        period = request.POST['period']

        student_timetable = StudentRegisteredClass.objects.get(user=user, week=week, period=period)
        student_points = StudentPoints.objects.get(user=user)

        # ポイントが足りなければ，登録失敗を返す
        if student_points.points <= 0:
            return False

        student_timetable.subject = subject
        student_points.points -= 1
        student_timetable.save()
        student_points.save()
        return True

        # register_result = register_student_subject(user, subject, week, period)

    def delete_class(self, request):
        week = request.POST['week']
        period = request.POST['period']
        delete_class = StudentRegisteredClass.objects.get(user=user, week=week, period=period)
        student_points = StudentPoints.objects.get(user=user)
        delete_class.subject = ""
        student_points.points += 1
        delete_class.save()
        student_points.save()


class StudentPoints(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=5)

@receiver(post_save, sender=User)
def create_student_data(sender, instance, created, **kwargs):
    if created:
        weeks = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
        periods = ['1', '2', '3', '4', '5']
        for period in periods:
            for week in weeks:
                record = StudentRegisteredClass(user=instance, week=week, period=period)
                record.save()
        record = StudentPoints(user=instance, points=5)
        record.save()
