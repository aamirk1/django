from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html',{'hm':'Home'})

def about(request):
    return render(request, 'core/about.html',{'ab':'About'})

def contact(request):
    return render(request, 'core/contact.html',{'co':'Contact'})

def top(request):
    return render(request, 'core/cour.html',{'p':'PHP'})