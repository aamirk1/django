
from django.contrib import admin
from django.urls import path
from course import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('learnpy/', views.learn_python),
    path('learnva/', views.learn_var),
    path('learnma/', views.learn_math),
    path('learnfo/', views.learn_format),
    
]
