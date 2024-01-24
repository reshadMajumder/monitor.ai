from django.db import models

# Create your models here.
class CourseName(models.Model):
    course_id = models.CharField(max_length=10 )
    name = models.CharField(max_length=100)
    description= models.CharField(max_length=300)
    def __str__(self):
        return self.name
class StudentStatus(models.Model):
    course=models.ForeignKey(CourseName,on_delete=models.CASCADE)
    photo=models.ImageField()
    name=models.CharField(max_length=100)
    classTime=models.IntegerField()
    performence=models.IntegerField()
    status=models.BooleanField(default=False)





    