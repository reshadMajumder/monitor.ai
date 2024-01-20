# core/views.py
from django.shortcuts import render
from teachers.models import Teacher

def home(request):
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'teachers': teachers})
