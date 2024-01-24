# core/views.py
from django.shortcuts import render
from teachers.models import Teacher
from teacherAdminPanel.models import CourseName

def home(request):
    teachers = Teacher.objects.all()
    course=CourseName.objects.all()
    return render(request, 'home.html', context={'teachers': teachers,'courses':course})
