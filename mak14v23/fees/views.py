from django.shortcuts import render

# Create your views here.
def f_py(request):
    return render(request, 'fees/feesone.html',{'fp':3500})

def f_ja(request):
    return render(request, 'fees/feestwo.html',{'fj':4500})