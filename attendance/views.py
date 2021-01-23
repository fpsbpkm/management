from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm,SignInForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Subject, StudentRegisteredClass, StudentPoints
from .register import register_student_subject, delete_student_subject

@login_required
def timetable(request):
    user = request.user
    # 借りの処理
    register_result = True
    if request.method == 'POST':
        # 登録処理（ifの条件が良くないかも）
        if request.POST["subject"] != '削除':
            register_result = StudentRegisteredClass.register_class(request)
        # 削除処理
        elif request.POST["subject"] == "削除":
            StudentRegisteredClass.delete_class(request)

    student_timetable = StudentRegisteredClass.objects.filter(user=user)
    student_points = StudentPoints.objects.get(user=user)
    context = {'user':user, 'student_timetable':student_timetable, 
                'student_points':student_points,'register_result':register_result}
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
            # ユーザが入力したフォーム内容をデータベースに保存
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
