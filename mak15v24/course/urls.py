from django.urls import path
from . import views
urlpatterns = [
    path('corone/', views.courseone),
    path('cortwo/', views.coursetwo),
]