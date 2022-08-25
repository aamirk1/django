from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees_java(request):
    return HttpResponse(10000)

def fees_py(request):
    return HttpResponse(15000)
