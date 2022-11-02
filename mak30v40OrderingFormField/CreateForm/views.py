from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showdata(request):
    fm = StudentRegistration()
    fm.order_fields(field_order=['name','last_name','email'])
    #line 7 this method is used to ordering the label by default field_order = None
    return render(request, 'CreateForm/createForm.html',{'frm':fm})