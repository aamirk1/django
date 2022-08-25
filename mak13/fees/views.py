from django.shortcuts import render

# Create your views here.
def fees_python(request):
    return render(request,'fees/fees1.html',)

def fees_java(request):
    return render(request,'fees/fees2.html',{'fe':'Java fees = 300 '})