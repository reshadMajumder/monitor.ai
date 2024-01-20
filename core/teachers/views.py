from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

# views.py
from django.shortcuts import render
from .models import Teacher, AcademicQualification, WorkExperience, TeachingRoutine

def teacher_profile(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        academic_qualifications = AcademicQualification.objects.filter(teacher=teacher)
        work_experiences = WorkExperience.objects.filter(teacher=teacher)
        teaching_routines = TeachingRoutine.objects.filter(teacher=teacher)

        context = {
            'teacher': teacher,
            'academic_qualifications': academic_qualifications,
            'work_experiences': work_experiences,
            'teaching_routines': teaching_routines,
        }

        return render(request, 'teachers_profile.html', context)
    except Teacher.DoesNotExist:
        return HttpResponse("Teacher does not exist",status=404)
