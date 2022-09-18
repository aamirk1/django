from django.urls import path
from . import views

urlpatterns = [
    path('feespy/',views.f_py),
    path('feesja/',views.f_ja)
]
