from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
   path("", views.Name, name='Name'),
    path("about/", views.About, name='About'),
    path("contacts/", views.Contacts, name='Contacts'),
    path("home/", views.Home, name='Home'),
    path("portfolio/", views.Portfolio, name='Portfolio'),
    
]



