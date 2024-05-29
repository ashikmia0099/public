from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('Course-Detail-Page/<int:id>/',views.CourseDetailsPage, name='CourseDetailsPage'),
   
   
]
