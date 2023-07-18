from django.shortcuts import render,redirect
from home.models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,'home/home.html')

def createTodo(request):
    if request.method == "POST":
        user = request.user
        task_name = request.POST.get('taskName')
        desc = request.POST.get('description')
        priority = request.POST.get('priority')
        lastDate = request.POST.get('lastdate')
        tag = request.POST.get('tag')
        status = request.POST.get('status')

        todo = Todo(user=user,task_name=task_name,description=desc,priority=priority,dueDate=lastDate,tag=tag,status=status)        
        todo.save()
        pass
    return render(request,'home/createTodo.html')

def editTodo(request,id):
    currDetails = Todo.objects.filter(sno=id).first()
    if request.method == "POST":
        newtask_name = request.POST.get('newTaskName')
        newdesc = request.POST.get('newDescription')
        newpriority = request.POST.get('newPriority')
        newlastDate = request.POST.get('newLastdate')
        newtag = request.POST.get('newTag')
        newstatus = request.POST.get('newStatus')

        current = Todo.objects.get(sno=id)
        current.task_name = newtask_name
        current.description = newdesc
        current.priority = newpriority
        current.dueDate = newlastDate
        current.tag = newtag
        current.status = newstatus
        current.save()
        return redirect(f'/todo/{newtask_name}')

    return render(request,'home/editTodo.html',{'currDetails':currDetails})

def signInUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        choosePassword = request.POST.get('choosePassword')
        confirmPassword = request.POST.get('confirmPassword')

        if choosePassword != confirmPassword:
            return redirect('/signin/')
        
        user = User.objects.create_user(username=username,email=email,password=choosePassword)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect('/')
    return render(request,'home/signin.html')

def loginUser(request):
    if request.method == "POST":
        loginUsername = request.POST.get('loginUsername')
        loginPassword = request.POST.get('loginPassword')

        user = authenticate(username=loginUsername,password=loginPassword)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/login/')
        
    return render(request,'home/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def search(request):
    
    query = request.GET.get('search')
    if len(query)<=0 or len(query)>70:
        allTodos = []
    else: 
        user = request.user
        qTask_name = Todo.objects.filter(task_name__icontains=query, user=user)
        qDesc = Todo.objects.filter(description__icontains=query, user=user)
        qPriority = Todo.objects.filter(priority__icontains=query, user=user)
        qLastdate = Todo.objects.filter(dueDate__icontains=query, user=user)
        qTag = Todo.objects.filter(tag__icontains=query, user=user)
        qStatus = Todo.objects.filter(status__icontains=query, user=user)
        allTodos = qTask_name | qDesc | qPriority | qLastdate | qTag | qStatus

    context = {
        'result': allTodos,
        'query': query
    }


    return render(request, 'home/search.html', context)

def deleteTask(request,id):
    todo = Todo.objects.get(sno=id)
    todo.delete()

    return redirect('/todo/')