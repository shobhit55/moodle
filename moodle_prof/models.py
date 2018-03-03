from django.db import models
from accounts.models import User

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=40)
    course_code=models.CharField(max_length=40)
   # message=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

class course1(models.Model):
    course_name = models.CharField(max_length=40)
    course_code = models.CharField(max_length=40)
   # message=models.CharField(max_length=255)
    user = models.ManyToManyField(User, default=None)

class message(models.Model):
    user=models.ManyToManyField(User,default=None)
    course=models.ForeignKey(course1,on_delete=models.CASCADE)
    message=models.CharField(max_length=255)