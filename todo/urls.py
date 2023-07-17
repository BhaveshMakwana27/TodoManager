from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.todo,name='todos'),
    path('<str:slug>',views.todoDetails,name='TodoDetails'),
    
]
