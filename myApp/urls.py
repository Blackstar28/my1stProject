from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
   path("", views.helloworld, name='helloworld'),
    path("testpath/", views.testPath, name='testPath'),
    path("testpath/1", views.testPath1, name='testPath')
]
