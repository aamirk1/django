from django.shortcuts import render

# Create your views here.

def home(request):
    fess = {'title':'home','hm':'Home'}
    return render(request, "home.html",fess)