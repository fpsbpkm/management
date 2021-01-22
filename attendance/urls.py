from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('timetable', views.timetable, name='timetable'),
    path('select_subject', views.select_subject, name='select_subject'),
    # sign upのビューは提供されていないので，自作する必要がある
    path('signup', views.signup, name='signup'),
    # login,logoutのビューは提供されているため，テンプレートのみ作れば良い
    path('login', auth_views.LoginView.as_view(template_name="attendance/login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name="attendance/logout.html"), name='logout'),
]