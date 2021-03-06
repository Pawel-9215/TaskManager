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

PUBLISHED = (
    (0, "NotPublished"),
    (1, "Published"),
)

class Devlog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    created_on = DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=4096)
    status = models.IntegerField(choices=PUBLISHED, default = 0)

    class Meta:
        ordering = ['created_on']

    def __str__(self) -> str:
        return self.title[:12]+"(...)"

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
    deadline_in = DateTimeField(null=True)
    status = models.IntegerField(choices=STATUS, default = 0)

    class Meta:
        ordering = ['created_on']

    def __str__(self) -> str:
        return self.title

    def update(self):
        self.updated_on = timezone.now()
        self.save()

    def is_week_old(self):
        if self.deadline_in is not None:
            days_to_deadline = (self.deadline_in - timezone.now()).days
            print(self, days_to_deadline)
            return 0 > days_to_deadline
        else:
            return False

    