from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Home Page')

def learn_python(request):
    return HttpResponse('<h1>Hello World</h1>')

def learn_var(request):
    a = '<h1>Hello India</h1>'
    return HttpResponse(a)

def learn_math(reqtuest):
    a = 30+40
    return HttpResponse(a)
def learn_format(request):
    a = 'Mak'
    return HttpResponse(f'Hello How r u {a}')