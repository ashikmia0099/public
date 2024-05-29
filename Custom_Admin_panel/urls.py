from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('custom-admin-panel',views.Admin_panel_view, name='customadmin' )
    
   
   
]
