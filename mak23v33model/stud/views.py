from django.shortcuts import render

# Create your views here.
def studata(request):
    return render(request, 'stud/student_data.html',{'no':'model view v33'})