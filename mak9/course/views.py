from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_py(request):
    return HttpResponse("<h1>Python</h1>")

def learn_ja(request):
    return HttpResponse("<h1>Java</h1>")