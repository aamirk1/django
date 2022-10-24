from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=90)
    stuemail = models.CharField(max_length=90)
    stupass = models.CharField(max_length=90)