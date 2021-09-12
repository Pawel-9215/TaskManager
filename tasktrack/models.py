from typing import Optional
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.utils import timezone
import datetime

# Create your models here.
STATUS = (
    (0, "ToDo"),
    (1, "Done"),
)

class Project(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=24, unique=True)
    status = models.IntegerField(choices=STATUS, default = 0)

    def __str__(self) -> str:
        return self.title

class Task(models.Model):
    
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    project = models.ForeignKey('tasktrack.Project', related_name='tasks', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, unique=True)
    # author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'tasks')
    updated_on = models.DateTimeField(auto_now = True)
    description = models.TextField(max_length=512)
    created_on = DateTimeField(auto_now_add=True)
    deadline_in = models.IntegerField(null=True, default=5)
    status = models.IntegerField(choices=STATUS, default = 0)

    class Meta:
        ordering = ['created_on']

    def __str__(self) -> str:
        return self.title

    def update(self):
        self.updated_on = timezone.now()
        self.save()

    def is_week_old(self):
        return (timezone.now() - self.created_on).days > self.deadline_in

    