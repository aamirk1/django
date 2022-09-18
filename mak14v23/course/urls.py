from django.urls import path
from . import views

urlpatterns = [
    path('learnpy/',views.c_py),
    path('learnja/',views.c_ja),
]
