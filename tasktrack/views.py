from django.contrib import auth
from django.shortcuts import render, redirect
from django.views import generic
from .models import Project, STATUS, Task, Devlog
from django.contrib.auth.mixins import LoginRequiredMixin
from tasktrack.forms import TaskForm, ProjectForm
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import datetime

# Create your views here.

class UserLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('task_list')

class UserRegister(generic.FormView):
    template_name = 'register.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task_list')
        return super(UserRegister, self).get(*args, **kwargs)

class DevLog(generic.ListView):
    model = Devlog
    queryset = Devlog.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'devlog'
    template_name = 'devlog.html'

class TaskList(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Task
    # queryset = Task.objects.filter(status=0).order_by('created_on')
    context_object_name = 'task_list'
    template_name = "task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(author=self.request.user)
        context['task_list'] = context['task_list'].filter(status=0).order_by('created_on')
        context['projects'] = Project.objects.filter(owner=self.request.user)
        context['current_date'] = datetime.datetime.now()
        return context

class ProjectList(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Project
    context_object_name = 'project_list'
    template_name = 'project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = context['project_list'].filter(owner=self.request.user)
        return context

class AboutView(generic.TemplateView):
    template_name = "about.html"

class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'task_list.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(owner=self.request.user)
        return context

class TaskListDone(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Task
    #queryset = Task.objects.filter(status=1).order_by('created_on')
    context_object_name = 'task_list'
    template_name = "task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(author=self.request.user)
        context['task_list'] = context['task_list'].filter(status=1).order_by('created_on')
        context['projects'] = Project.objects.filter(owner=self.request.user)
        return context

class TaskEditView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(TaskEditView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    

class CreateTaskView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'task_list.html'

    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'task_form.html'

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(CreateTaskView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateTaskView, self).form_valid(form)

class CreateProjectView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'task_list.html'

    form_class = ProjectForm
    model = Project
    success_url = reverse_lazy('task_list')
    template_name = 'project_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateProjectView, self).form_valid(form)

class ProjectEditView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        obj = self.get_object()
        # since status is 0, 1 not comparing like status == 1
        if form.cleaned_data.get('status'):
            obj.tasks.update(status=1)
        return super().form_valid(form)


class DeleteProjectView(LoginRequiredMixin, generic.DeleteView):
    login_url = '/login/'
    model = Project
    template_name='project_delete.html'
    success_url = reverse_lazy('project_list')