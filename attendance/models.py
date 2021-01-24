from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    week = models.CharField(max_length=10)
    period = models.CharField(max_length=10)


class Student(AbstractUser):
    points = models.IntegerField(default=5)

    def get_points(self):
        return self.points

    def decrement_point(self):
        self.points -= 1
        self.save()

    def increment_point(self):
        self.points += 1
        self.save()


class StudentRegisteredClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, unique=False)
    week = models.CharField(max_length=10)
    period = models.CharField(max_length=10)
    subject = models.CharField(max_length=30, blank=True)

    @classmethod
    def register_class(cls, request):
        student = request.user
        subject = request.POST['subject']
        week = request.POST['week']
        period = request.POST['period']
        student_timetable = StudentRegisteredClass.objects.get(student=student, week=week, period=period)
        points = student.get_points()

        # ポイントが足りなければ，登録失敗を返す
        if points <= 0:
            return False

        student_timetable.subject = subject
        student.decrement_point()
        student_timetable.save()
        return True

    @classmethod
    def delete_class(cls, request):
        student = request.user
        week = request.POST['week']
        period = request.POST['period']
        student_timetable = StudentRegisteredClass.objects.get(student=student, week=week, period=period)
        student_points = student.get_points()
        student_timetable.subject = ""
        student.increment_point()
        student_timetable.save()


@receiver(post_save, sender=Student)
def create_student_data(sender, instance, created, **kwargs):
    if created:
        weeks = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
        periods = ['1', '2', 
                    '3', '4', '5']
        for period in periods:
            for week in weeks:
                record = StudentRegisteredClass(student=instance, week=week, period=period)
                record.save()
