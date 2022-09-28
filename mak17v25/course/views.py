from django.shortcuts import render

# Create your views here.
def learn_py(request):
    cr = {'cname':'Python',"title":'cname_st'}
    return render(request, 'course/course_st.html', cr)

def learn_ml(request):
    list1 = {'title':'course_nd','cname':'Machine Learning'}
    return render(request, 'course/course_nd.html',list1)