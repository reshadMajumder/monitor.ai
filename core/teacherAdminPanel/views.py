from django.shortcuts import render
from .models import CourseName,StudentStatus
# Create your views here.

def panel(request,courseId):

    course=CourseName.objects.get(pk=courseId)
    Studentst=StudentStatus.objects.filter(course=course)
    context={'course':course,'students':Studentst}

    return render(request, 'teacherAdminPanel.html',context)