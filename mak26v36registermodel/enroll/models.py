from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=90)
    stu_email = models.EmailField(max_length=20)
    stu_pass = models.CharField(max_length=20)
    
    def __str__(self):
        return self.stu_name    # this method is used to show name in admin panel
    