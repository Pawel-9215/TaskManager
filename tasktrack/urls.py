from . import views
from django.urls import  path

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('task_done/', views.TaskListDone.as_view(), name='task_done'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('create_task/', views.CreateTaskView.as_view(), name='create_task'),
]