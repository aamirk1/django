from django.shortcuts import render

# Create your views here.
def learn_python(request):

    coursename = {'cname':'Django'}

    return render(request,'course/course1.html',context=coursename)

def learn_java(request):
    cname = 'C++'
    duration = '6 month'
    seat = 15
    django_details = {'nm':cname,'du':duration,'st':seat}
    return render(request,'course/course2.html',context = django_details)