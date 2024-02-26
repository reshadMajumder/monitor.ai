from django.shortcuts import render

# Create your views here.


from teacherAdminPanel.models import Students

def studentsPerformence(request):


    section=Students.objects.all()


    context={
        "section":section}
    
    return  render (request,"performence.html",context)