from django.urls import path
from .import views
urlpatterns = [
    path('feesfv/',views.learn_fees),
]