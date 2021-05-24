from django.shortcuts import render
from django.views import generic
from .models import Project, STATUS, Task
from django.contrib.auth.mixins import LoginRequiredMixin
from tasktrack.forms import TaskForm, ProjectForm

# Create your views here.

class TaskList(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Task
    queryset = Task.objects.filter(status=0).order_by('created_on')
    template_name = "task_list.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"

class TaskListDone(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Task
    queryset = Task.objects.filter(status=1).order_by('created_on')
    template_name = "done_tasks.html"

class CreateTaskView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'task_list.html'

    form_class = TaskForm
    model = Task

class CreateProjectView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'task_list.html'

    form_class = ProjectForm
    model = Project