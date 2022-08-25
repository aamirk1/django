from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees_py(request):
    return HttpResponse("<h1>1500</h1>")

def fees_ja(request):
    return HttpResponse("<h1>1000</h1>")