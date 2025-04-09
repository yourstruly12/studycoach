from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
from .forms import TaskForm

def home(request):
    return render(request, 'studycoach/home.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'studycoach/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'studycoach/add_task.html', {'form': form})

def pomodoro(request):
    return render(request, 'studycoach/pomodoro.html')

def study_plan(request):
    return render(request, 'studycoach/study_plan.html')

def motivation(request):
    return render(request, 'studycoach/motivation.html')

def progress(request):
    return render(request, 'studycoach/progress.html')

def reminders(request):
    return render(request, 'studycoach/reminders.html')

def add_reminder(request):
    return HttpResponse("Reminder added successfully!")

def adjust_plan(request):
    return HttpResponse("Adjust your study plan here!")
