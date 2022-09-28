from django.urls import path
from . import views
urlpatterns = [
    path('feeso/',views.fees_py),
    path('feest/',views.fees_ja),
]
