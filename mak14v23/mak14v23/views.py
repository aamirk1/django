from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{'hm':'this is home page'})
