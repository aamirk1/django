from django.shortcuts import render
from datetime import datetime
# Create your views here.
def learn_python(request):
    #d = datetime.now()
    student = {'names':['Rahul','shikhar','Sanju','chahal','deepak']}
    return render(request,'course/course1.html',student)

def learn_java(request):
    stu = {'stu1': {'name':'Rahul','roll':11},
           'stu2': {'name':'Raj','roll':12},
           'stu3': {'name':'Rohit','roll':13},
           'stu4': {'name':'Raju','roll':14},
    }
    student =  {'student':stu}
    
    return render(request,'course/course2.html',student)