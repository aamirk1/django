from django.urls import path
from . import views
urlpatterns = [
    path('feone/', views.feesone),
    path('fetwo/', views.feestwo),
]