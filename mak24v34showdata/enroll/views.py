from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def stu_details(request):
    stu = Student.objects.all() #this method used to retrieve  all data
    stud = Student.objects.get(pk=1) #this method used to retrieve any specific data and pk means primary key
    return render(request, 'enroll/stu_details.html',{'st':stu,'stus':stud})
