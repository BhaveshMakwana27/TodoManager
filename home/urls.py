from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home,name='Home'),
    path('signin',views.signIn,name='SignIn'),
    path('login',views.login,name='LogIn'),
    path('createTodo',views.createTodo,name='CreateTodo'),
    path('editTodo',views.editTodo,name='EditTodo')
]