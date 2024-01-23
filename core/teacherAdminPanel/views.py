from django.shortcuts import render
from .models import*
# Create your views here.

def panel(request,courseId):

    course=CourseName.objects.get(pk=courseId)
    context={'course':course}
    return render(request, 'teacherAdminPanel.html',context)