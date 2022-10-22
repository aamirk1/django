from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mains/home.html',{'hm':'Home'})

def about(request):
    return render(request, 'mains/about.html',{'ab':'About'})

def contact(request):
    return render(request, 'mains/contact.html',{'co':'Contact'})