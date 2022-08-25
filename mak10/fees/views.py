from django.shortcuts import render

# Create your views here.
def fees_py(request):
    return render(request,'fees1.html')

def fees_ja(request):
    return render(request,'fees2.html')