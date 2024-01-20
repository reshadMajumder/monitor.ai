from django.db import models

# Create your models here.


from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
    
    def __str__(self):
        return self.name

class AcademicQualification(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    university = models.CharField(max_length=255)

class WorkExperience(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)

class TeachingRoutine(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=255)
