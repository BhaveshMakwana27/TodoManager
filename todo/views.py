from django.shortcuts import render,redirect
from home.models import Todo

def todo(request):
    user = request.user
    if request.user.is_anonymous :
        return redirect('/')
    todoList = Todo.objects.filter(user=user).order_by('dueDate')
    return render(request,'todo/todoList.html',{'todoList':todoList})

def todoDetails(request,slug):
    detail = Todo.objects.filter(task_name=slug).first()
    return render(request,'todo/todoDetails.html',{'slug':slug,'details':detail})
