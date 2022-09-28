from django.shortcuts import render

# Create your views here.
def fees_py(request):
    fes = {'title':'feesone','fe1':300}
    return render(request, "fees/fees_st.html",fes)

def fees_ja(request):
    fess = {'title':'feestwo','fe2':500}
    return render(request, "fees/fees_nd.html",fess)