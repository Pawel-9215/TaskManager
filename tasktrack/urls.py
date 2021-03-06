from . import views
from django.urls import  path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('project_list', views.ProjectList.as_view(), name='project_list'),
    path('task_done/', views.TaskListDone.as_view(), name='task_done'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('create_task/', views.CreateTaskView.as_view(), name='create_task'),
    path('edit_task/<int:pk>', views.TaskEditView.as_view(), name='edit_task'),
    path('edit_project/<int:pk>', views.ProjectEditView.as_view(), name='edit_project'),
    path('delete/<int:pk>', views.DeleteProjectView.as_view(), name='delete_project'),
    path('create_project/', views.CreateProjectView.as_view(), name='create_project'),
    path('project_detail/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('news/', views.DevLog.as_view(), name='devlog')
]