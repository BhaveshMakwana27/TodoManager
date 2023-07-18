from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='Home'),
    path('login/',views.loginUser,name='LogIn'),
    path('logout/',views.logoutUser,name='Logout'),
    path('signin/',views.signInUser,name='SignIn'),
    path('createTodo/',views.createTodo,name='CreateTodo'),
    path('editTodo/<int:id>',views.editTodo,name='EditTodo'),
    path('delete/<int:id>',views.deleteTask,name='DeleteTask'),
    path('search/',views.search,name='Search'),
]