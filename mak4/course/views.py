from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_course(request):
    return HttpResponse("Python")