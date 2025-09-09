from django import forms
from django.contrib.auth.models import User
from .models import Project, Task


class ProjectForm(forms.ModelForm):
    """Form for creating and updating projects."""
    
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'completed']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter project description'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'name': 'Project Name',
            'description': 'Description',
            'start_date': 'Start Date',
            'end_date': 'End Date (Optional)',
            'completed': 'Mark as Completed',
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError(
                "End date cannot be earlier than start date."
            )
        
        return cleaned_data


class TaskForm(forms.ModelForm):
    """Form for creating and updating tasks."""
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'assigned_to', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter task description (optional)'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
            'assigned_to': forms.Select(attrs={
                'class': 'form-select'
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Description (Optional)',
            'due_date': 'Due Date (Optional)',
            'priority': 'Priority',
            'assigned_to': 'Assigned To (Optional)',
            'completed': 'Mark as Completed',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show active users in the assigned_to field
        self.fields['assigned_to'].queryset = User.objects.filter(is_active=True)
        self.fields['assigned_to'].empty_label = "Select user (optional)"

    def clean(self):
        cleaned_data = super().clean()
        due_date = cleaned_data.get('due_date')
        
        if due_date:
            from django.utils import timezone
            if due_date < timezone.now().date():
                raise forms.ValidationError(
                    "Due date cannot be in the past."
                )
        
        return cleaned_data


class TaskQuickCreateForm(forms.ModelForm):
    """Simplified form for quickly creating tasks."""
    
    class Meta:
        model = Task
        fields = ['title', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'title': 'Task Title',
            'priority': 'Priority',
        }
