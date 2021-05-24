from . import views
from django.urls import  path

urlpatterns = [
    path('task_list/', views.TaskList.as_view(), name='task_list'),
    path('task_done/', views.TaskListDone.as_view(), name='task_done'),
]