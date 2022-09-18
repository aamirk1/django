from django.shortcuts import render

# Create your views here.
def c_py(request):
    return render(request, 'course/courseone.html',{'cp':'Python'})

def c_ja(request):
    return render(request, 'course/coursetwo.html',{'cj':'Java'})