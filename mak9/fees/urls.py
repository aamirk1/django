from django.urls import path
from .import views
urlpatterns = [
    path('feespy/',views.fees_py),
    path('feesja/',views.fees_ja)
]