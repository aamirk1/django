from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def roll(request):
    stu = Student.objects.all()
    return render(request, 'home.html',{'st':stu})