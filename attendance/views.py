from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm,SignInForm
from django.contrib.auth.decorators import login_required

from django.views import generic
from .models import Subject, Student
from .register import register_student_subject, delete_student_subject

@login_required
def timetable(request):
    user = request.user
    # 借りの処理
    register_result = True

    if request.method == 'POST':

        # 科目を登録するの場合
        if request.POST["subject"] != '削除':
            subject = request.POST['subject']
            week = int(request.POST['week'])
            time = int(request.POST['time'])
            register_result = register_student_subject(user, subject, week, time)

        # 登録削除の処理
        elif request.POST["subject"] == "削除":
            week = int(request.POST['week'])
            time = int(request.POST['time'])
            delete_student_subject(user, week, time)
    
    student = Student.objects.get(user=user)

    context = {'user':user, 'student':student, 'register_result':register_result}
    return render(request, 'attendance/timetable.html', context)

def select_subject(request):
    if request.method == 'POST':
        week = request.POST['week']
        time = request.POST['time']
        subjects = Subject.objects.filter(week=week, time=time)
        context = {'week':week, 'time':time, 'subjects':subjects}
        return render(request, 'attendance/select_subject.html', context)
    else:
        return render(request, 'attendance/select_subject.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable')
    else:
        form = SignUpForm()
    
    context = {'form':form}
    return render(request, 'attendance/signup.html', context)

def sign_in(request):
    form = SignInForm()
    context = {'form':form}
    return render(request, 'attendance/sign_in.html', context)
