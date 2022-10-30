from django.contrib import admin
from modeladmin.models import Student
# Register your models here.

@admin.register(Student)    # register your models here using decorator

#line 5 and 11 are same

class StudentAdmin(admin.ModelAdmin): # this is model admin class
    list_display=('stu_id','stu_name','stu_email','stu_pass')   #alway type here in tuple or list format only
# admin.site.register(Student,StudentAdmin)