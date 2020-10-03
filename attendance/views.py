from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm,SignInForm
from django.contrib.auth.decorators import login_required

from django.views import generic
from .models import Subject, StudentTimetable, StudentPoints
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
            week = request.POST['week']
            period = request.POST['period']
            # データベースに登録
            register_result = register_student_subject(user, subject, week, period)

        # 登録削除の処理
        elif request.POST["subject"] == "削除":
            week = request.POST['week']
            period = request.POST['period']
            delete_student_subject(user, week, period)
    weeks = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
    periods = ['period1', 'period2', 
                    'period3', 'period4', 'period5']

    student_timetable = StudentTimetable.objects.filter(user=user)
    student_points = StudentPoints.objects.get(user=user)
    sorted_data = []
    for period in periods:
        for week in weeks:
            s = StudentTimetable.objects.filter(user=user, week=week, period=period)
            sorted_data.extend(s)
    
    context = {'user':user, 'sorted_data':sorted_data, 'student_points':student_points,'register_result':register_result}
    return render(request, 'attendance/timetable.html', context)

def select_subject(request):
    if request.method == 'POST':
        week = request.POST['week']
        period = request.POST['period']
        subjects = Subject.objects.filter(week=week, period=period)
        context = {'week':week, 'period':period, 'subjects':subjects}
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
