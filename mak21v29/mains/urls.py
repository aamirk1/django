from django.urls import path
from . import views
urlpatterns = [
    path('about/',views.about,name="aboutus"),
    path('contact/',views.contact,name="contactus")
]
