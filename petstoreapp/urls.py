from django.urls import path
from . import views

#create views and then add the view pages to thwe path

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pets_list, name='pet_list'),
    path('pets/create/', views.pet_create, name='pet_create'),
    path('search/', views.search_results, name='search_results'),
]