from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinLengthValidator


class Project(models.Model):
    """Project model for managing project information."""
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3)],
        help_text="Enter a descriptive project name (minimum 3 characters)"
    )
    description = models.TextField(
        help_text="Provide a detailed description of the project"
    )
    start_date = models.DateField(
        default=timezone.now,
        help_text="When did this project start?"
    )
    end_date = models.DateField(
        null=True, 
        blank=True,
        help_text="When is this project expected to end? (optional)"
    )
    completed = models.BooleanField(
        default=False,
        help_text="Is this project completed?"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='created_projects',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

    @property
    def is_overdue(self):
        """Check if project is overdue."""
        if self.end_date and not self.completed:
            return timezone.now().date() > self.end_date
        return False

    @property
    def completion_percentage(self):
        """Calculate project completion percentage based on tasks."""
        total_tasks = self.tasks.count()
        if total_tasks == 0:
            return 0
        completed_tasks = self.tasks.filter(completed=True).count()
        return round((completed_tasks / total_tasks) * 100, 1)


class Task(models.Model):
    """Task model for managing individual tasks within projects."""
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='tasks',
        help_text="Select the project this task belongs to"
    )
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3)],
        help_text="Enter a descriptive task title (minimum 3 characters)"
    )
    description = models.TextField(
        blank=True, 
        null=True,
        help_text="Provide additional details about this task (optional)"
    )
    completed = models.BooleanField(
        default=False,
        help_text="Is this task completed?"
    )
    due_date = models.DateField(
        null=True, 
        blank=True,
        help_text="When should this task be completed? (optional)"
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
        help_text="Set the priority level for this task"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    assigned_to = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks',
        help_text="Who is responsible for this task? (optional)"
    )

    class Meta:
        ordering = ['priority', 'due_date', 'created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"{self.title} ({self.project.name})"

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.project.pk})

    @property
    def is_overdue(self):
        """Check if task is overdue."""
        if self.due_date and not self.completed:
            return timezone.now().date() > self.due_date
        return False

    @property
    def priority_color(self):
        """Return Bootstrap color class based on priority."""
        color_map = {
            'low': 'success',
            'medium': 'info',
            'high': 'warning',
            'urgent': 'danger',
        }
        return color_map.get(self.priority, 'secondary')