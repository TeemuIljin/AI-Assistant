from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('add/', views.ProjectCreateView.as_view(), name='project_add'),  # Add a project
    path('<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),  # Edit a project
    path('<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),  # Delete a project
]

