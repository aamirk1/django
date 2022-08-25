from django.urls import path
from .import views
urlpatterns = [
    path('learnpy/',views.learn_python),
    path('learnja/',views.learn_java)
]
