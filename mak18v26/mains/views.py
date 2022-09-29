from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mains/home.html',{'hm':'Home'})

def home(request):
    return render(request, 'mains/about.html',{'ab':'About'})

def home(request):
    return render(request, 'mains/contact.html',{'co':'Contact'})