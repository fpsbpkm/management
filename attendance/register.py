from .models import StudentRegisteredClass, StudentPoints

def register_student_subject(user, subject, week, period):
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
   

def delete_student_subject(user, week, period):
    student_timetable = StudentRegisteredClass.objects.get(user=user, week=week, period=period)
    student_points = StudentPoints.objects.get(user=user)
    student_timetable.subject = ""
    student_points.points += 1
    student_timetable.save()
    student_points.save()
