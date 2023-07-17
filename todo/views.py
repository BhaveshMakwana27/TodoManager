from django.shortcuts import render,HttpResponse

def todo(request):
    return render(request,'todo/todoList.html')

def todoDetails(request,slug):
    return render(request,'todo/todoDetails.html',{'slug':slug})
