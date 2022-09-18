from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse('Home Page')

# def learn_python(request):
#     return HttpResponse('<h1>Hello World</h1>')

# def learn_var(request):
#     a = '<h1>Hello India</h1>'
#     return HttpResponse(a)

# def learn_math(reqtuest):
#     a = 30+40
#     return HttpResponse(a)
# def learn_format(request):
#     a = 'Mak'
#     return HttpResponse(f'Hello How r u {a}')

def index(request):
    return HttpResponse('Hello Home')

def learn_python(request):
    return HttpResponse('<h3>Hello python</h3>')

def learn_var(request):
    b = '<h2>Hello india</h2>'
    return HttpResponse(b)

def learn_math(request):
    a = 40+10
    return HttpResponse(a)

def learn_format(request):
    formate = "Formate"
    return HttpResponse(f'Hello   {formate}')