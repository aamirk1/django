from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=100)
    stuemail = models.CharField(max_length=50)
    stupass = models.CharField(max_length=60)
    studiv = models.CharField(max_length=30,default="not Available")