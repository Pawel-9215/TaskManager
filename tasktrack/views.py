from django.shortcuts import render
from django.views import generic
from .models import Project, STATUS, Task
from django.contrib.auth.mixins import LoginRequiredMixin
from tasktrack.forms import TaskForm, ProjectForm
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

# Create your views here.

class UserLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('task_list')

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
    success_url = reverse_lazy('task_list')
    template_name = 'task_form.html'

class CreateProjectView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'task_list.html'

    form_class = ProjectForm
    model = Project
    success_url = reverse_lazy('task_list')
    template_name = 'project_form.html'