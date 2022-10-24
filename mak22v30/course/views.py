from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, 'course/info.html')

def courses(request):
    return render(request, 'course/courses.html')