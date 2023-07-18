from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    task_name = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.CharField(max_length=6)
    dueDate = models.DateField(auto_now=False, auto_now_add=False)
    tag = models.CharField(max_length=50)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.task_name +' of '+ self.user.username
    