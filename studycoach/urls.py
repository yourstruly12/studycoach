from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),  # Keep this one
    path('pomodoro/', views.pomodoro, name='pomodoro'),
    path('study_plan/', views.study_plan, name='study_plan'),
    path('motivation/', views.motivation, name='motivation'),
    path('progress/', views.progress, name='progress'),
    path('reminders/', views.reminders, name='reminders'),
    path('add_reminder/', views.add_reminder, name='add_reminder'),
    path('adjust_plan/', views.adjust_plan, name='adjust_plan'),
]
