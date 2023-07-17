from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'home/home.html')

def signIn(request):
    return render(request,'home/signin.html')

def login(request):
    return render(request,'home/login.html')


def createTodo(request):
    return render(request,'todo/createTodo.html')

def editTodo(request):
    return render(request,'todo/editTodo.html')

