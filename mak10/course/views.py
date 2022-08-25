from django.shortcuts import render

# Create your views here.
def learn_py(request):
    return render(request,'course.html')

def learn_ja(request):
    return render(request,'course2.html')