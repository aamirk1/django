from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showdata(request):
    fm = StudentRegistration(auto_id=True,label_suffix=':-',initial={'name':'Aamir'})
    # auto_id=True or auto_id='mak_%s' is used to customize id name in the form

    # if auto_id=False then remove label tag or id tag

    # label_suffix=':-' is used to customize Label colon in the form
    # initial={'name':'Aamir'} is used to give initial value in the input box
    return render(request, 'CreateForm/createForm.html',{'frm':fm})