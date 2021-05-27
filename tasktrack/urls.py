from . import views
from django.urls import  path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('task_done/', views.TaskListDone.as_view(), name='task_done'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('create_task/', views.CreateTaskView.as_view(), name='create_task'),
    path('create_project/', views.CreateProjectView.as_view(), name='create_project'),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout')
]