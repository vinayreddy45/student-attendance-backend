from django.urls import path
from . import views

urlpatterns = [
    path('attendance/add', views.AddAttandanceAPI.as_view(), name='add_attendance'),
    path('attendance/list', views.AttendanceListAPI.as_view()),
    path('subjects', views.SubjectListAPI.as_view())
]