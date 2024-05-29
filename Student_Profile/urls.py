from django.contrib import admin
from .  import views 
from django.urls import path

urlpatterns = [
    
    path('Student-Information/', views.Student_info, name='student_info'),
    path('Update-student-info/', views.ChangeInfo, name='student_dataUpdate'),
    path('Student-Certificate/', views.Student_Certificate_view, name='certificate'),
    
]
