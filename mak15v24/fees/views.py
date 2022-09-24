from django.shortcuts import render

# Create your views here.
def feesone(request):
    return render(request, 'fees/feesone.html', {'fe':5000})
    
def feestwo(request):
    return render(request, 'fees/feestwo.html', {'ft':4808303})