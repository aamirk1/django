from django.shortcuts import render

# Create your views here.
def courseone(request):
    return render(request, 'course/courseone.html', {'co':'courseone = Python'})

def coursetwo(request):
    return render(request, 'course/coursetwo.html', {'ct':'coursetwo = django'})