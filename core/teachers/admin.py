from django.contrib import admin

# Register your models here.
from .models import*
from teacherAdminPanel.models import*
admin.site.register(Teacher)
admin.site.register(AcademicQualification)
admin.site.register(WorkExperience)
admin.site.register(TeachingRoutine)
admin.site.register(CourseName)
admin.site.register(StudentStatus)
