from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q, Count, Case, When, IntegerField
from django.utils import timezone
from .models import Project, Task
from .forms import ProjectForm, TaskForm


class ProjectListView(ListView):
    """List view for projects with search and filtering capabilities."""
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Project.objects.select_related('created_by').prefetch_related('tasks')
        
        # Search functionality
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        
        # Filter by completion status
        status = self.request.GET.get('status')
        if status == 'completed':
            queryset = queryset.filter(completed=True)
        elif status == 'active':
            queryset = queryset.filter(completed=False)
        
        # Filter by overdue status
        overdue = self.request.GET.get('overdue')
        if overdue == 'true':
            today = timezone.now().date()
            queryset = queryset.filter(
                end_date__lt=today,
                completed=False
            )
        
        return queryset.annotate(
            task_count=Count('tasks'),
            completed_task_count=Count('tasks', filter=Q(tasks__completed=True))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['status_filter'] = self.request.GET.get('status', '')
        context['overdue_filter'] = self.request.GET.get('overdue', '')
        return context


class ProjectDetailView(DetailView):
    """Detail view for individual projects."""
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    
    def get_queryset(self):
        return Project.objects.select_related('created_by').prefetch_related('tasks__assigned_to')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        
        # Get tasks with priority ordering
        tasks = project.tasks.all().order_by('priority', 'due_date', 'created_at')
        
        context['tasks'] = tasks
        context['completed_tasks'] = tasks.filter(completed=True)
        context['pending_tasks'] = tasks.filter(completed=False)
        context['overdue_tasks'] = tasks.filter(
            due_date__lt=timezone.now().date(),
            completed=False
        )
        
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Create view for new projects."""
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Project created successfully!')
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Update view for existing projects."""
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Project updated successfully!')
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """Delete view for projects."""
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Project deleted successfully!')
        return super().delete(request, *args, **kwargs)


def task_create(request, project_pk):
    """Create a new task for a specific project."""
    project = get_object_or_404(Project, pk=project_pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()
    
    return render(request, 'projects/task_form.html', {
        'form': form,
        'project': project
    })


def task_update(request, pk):
    """Update an existing task."""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('project_detail', pk=task.project.pk)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'projects/task_form.html', {
        'form': form,
        'project': task.project,
        'task': task
    })


def task_delete(request, pk):
    """Delete a task."""
    task = get_object_or_404(Task, pk=pk)
    project_pk = task.project.pk
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('project_detail', pk=project_pk)
    
    return render(request, 'projects/task_confirm_delete.html', {
        'task': task
    })


def toggle_task_completion(request, pk):
    """Toggle task completion status."""
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    
    status = 'completed' if task.completed else 'marked as pending'
    messages.success(request, f'Task {status}!')
    
    return redirect('project_detail', pk=task.project.pk)
