from django.urls import path
from .import views
urlpatterns = [
    path('learncv/',views.learn_course),
]