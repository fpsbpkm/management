from .models import Student

def select_time(student, week, time):
    if week == 1:
        if time == 1:
            selected = student.monday1
        elif time == 2:
            selected = student.monday2
        elif time == 3:
            selected = student.monday3
        elif time == 4:
            selected = student.monday4
        elif time == 5:
            selected = student.monday5
    elif week == 2:
        if time == 1:
            selected = student.tuesday1
        elif time == 2:
            selected = student.tuesday2
        elif time == 3:
            selected = student.tuesday3
        elif time == 4:
            selected = student.tuesday4
        elif time == 5:
            selected = student.tuesday5
    elif week == 3:
        if time == 1:
            selected = student.wednesday1
        elif time == 2:
            selected = student.wednesday2
        elif time == 3:
            selected = student.wednesday3
        elif time == 4:
            selected = student.wednesday4
        elif time == 5:
            selected = student.wednesday5
    elif week == 4:
        if time == 1:
            selected = student.thursday1
        elif time == 2:
            selected = student.thursday2
        elif time == 3:
            selected = student.thursday3
        elif time == 4:
            selected = student.thursday4
        elif time == 5:
            selected = student.thursday5
    elif week == 5:
        if time == 1:
            selected = student.friday1
        elif time == 2:
            selected = student.friday2
        elif time == 3:
            selected = student.friday3
        elif time == 4:
            selected = student.friday4
        elif time == 5:
            selected = student.friday5
    elif week == 6:
        if time == 1:
            selected = student.saturday1
        elif time == 2:
            selected = student.saturday2
        elif time == 3:
            selected = student.saturday3
        elif time == 4:
            selected = student.saturday4
        elif time == 5:
            selected = student.saturday5
    elif week == 7:
        if time == 1:
            selected = student.sunday1
        elif time == 2:
            selected = student.sunday2
        elif time == 3:
            selected = student.sunday3
        elif time == 4:
            selected = student.sunday4
        elif time == 5:
            selected = student.sunday5
    
    return selected

def register_student_subject(user, subject, week, time):
    student = Student.objects.get(user=user)
    
    if student.points <= 0:
        return False
    if week == 1:
        if time == 1:
            student.monday1 = subject
        elif time == 2:
            student.monday2 = subject
        elif time == 3:
            student.monday3 = subject
        elif time == 4:
            student.monday4 = subject
        elif time == 5:
            student.monday5 = subject
    elif week == 2:
        if time == 1:
            student.tuesday1 = subject
        elif time == 2:
            student.tuesday2 = subject
        elif time == 3:
            student.tuesday3 = subject
        elif time == 4:
            student.tuesday4 = subject
        elif time == 5:
            student.tuesday5 = subject
    elif week == 3:
        if time == 1:
            student.wednesday1 = subject
        elif time == 2:
            student.wednesday2 = subject
        elif time == 3:
            student.wednesday3 = subject
        elif time == 4:
            student.wednesday4 = subject
        elif time == 5:
            student.wednesday5 = subject
    elif week == 4:
        if time == 1:
            student.thursday1 = subject
        elif time == 2:
            student.thursday2 = subject
        elif time == 3:
            student.thursday3 = subject
        elif time == 4:
            student.thursday4 = subject
        elif time == 5:
            student.thursday5 = subject
    elif week == 5:
        if time == 1:
            student.friday1 = subject
        elif time == 2:
            student.friday2 = subject
        elif time == 3:
            student.friday3 = subject
        elif time == 4:
            student.friday4 = subject
        elif time == 5:
            student.friday5 = subject
    elif week == 6:
        if time == 1:
            student.saturday1 = subject
        elif time == 2:
            student.saturday2 = subject
        elif time == 3:
            student.saturday3 = subject
        elif time == 4:
            student.saturday4 = subject
        elif time == 5:
            student.saturday5 = subject
    elif week == 7:
        if time == 1:
            student.sunday1 = subject
        elif time == 2:
            student.sunday2 = subject
        elif time == 3:
            student.sunday3 = subject
        elif time == 4:
            student.sunday4 = subject
        elif time == 5:
            student.sunday5 = subject
    student.points -= 1
    student.save()
    return True

def delete_student_subject(user, week, time):
    student = Student.objects.get(user=user)
    if week == 1:
        if time == 1:
            student.monday1 = ""
        elif time == 2:
            student.monday2 = ""
        elif time == 3:
            student.monday3 = ""
        elif time == 4:
            student.monday4 = ""
        elif time == 5:
            student.monday5 = ""
    elif week == 2:
        if time == 1:
            student.tuesday1 = ""
        elif time == 2:
            student.tuesday2 = ""
        elif time == 3:
            student.tuesday3 = ""
        elif time == 4:
            student.tuesday4 = ""
        elif time == 5:
            student.tuesday5 = ""
    elif week == 3:
        if time == 1:
            student.wednesday1 = ""
        elif time == 2:
            student.wednesday2 = ""
        elif time == 3:
            student.wednesday3 = ""
        elif time == 4:
            student.wednesday4 = ""
        elif time == 5:
            student.wednesday5 = ""
    elif week == 4:
        if time == 1:
            student.thursday1 = ""
        elif time == 2:
            student.thursday2 = ""
        elif time == 3:
            student.thursday3 = ""
        elif time == 4:
            student.thursday4 = ""
        elif time == 5:
            student.thursday5 = ""
    elif week == 5:
        if time == 1:
            student.friday1 = ""
        elif time == 2:
            student.friday2 = ""
        elif time == 3:
            student.friday3 = ""
        elif time == 4:
            student.friday4 = ""
        elif time == 5:
            student.friday5 = ""
    elif week == 6:
        if time == 1:
            student.saturday1 = ""
        elif time == 2:
            student.saturday2 = ""
        elif time == 3:
            student.saturday3 = ""
        elif time == 4:
            student.saturday4 = ""
        elif time == 5:
            student.saturday5 = ""
    elif week == 7:
        if time == 1:
            student.sunday1 = ""
        elif time == 2:
            student.sunday2 = ""
        elif time == 3:
            student.sunday3 = ""
        elif time == 4:
            student.sunday4 = ""
        elif time == 5:
            student.sunday5 = ""
    student.points += 1
    student.save()
