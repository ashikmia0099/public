from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeView, name= 'homepage'),
    path('category/<slug:category_slug>/',views.HomeView, name = 'cattegory_wise_sort'),
    path('Category-Page/<int:id>/', views.detail_category_page, name='category_page'),
    
    
    
    
    
]
