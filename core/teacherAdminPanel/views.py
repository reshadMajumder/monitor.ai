from django.shortcuts import render
from .models import*
# Create your views here.

def tpanel(request):
   
    return render(request, 'teacherAdminPanel.html')