from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # Project URLs
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('add/', views.ProjectCreateView.as_view(), name='project_add'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    
    # Task URLs
    path('<int:project_pk>/tasks/add/', views.task_create, name='task_add'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:pk>/toggle/', views.toggle_task_completion, name='task_toggle'),
]

