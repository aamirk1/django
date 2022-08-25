from django.urls import path
from . import views
urlpatterns = [
    path('learnpy/',views.learn_py),
    path('learnja/',views.learn_ja)
]