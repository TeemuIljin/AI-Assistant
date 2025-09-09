from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'start_date', 'end_date', 'completion_percentage', 'completed', 'is_overdue']
    list_filter = ['completed', 'created_at', 'start_date', 'end_date', 'created_by']
    search_fields = ['name', 'description', 'created_by__username']
    readonly_fields = ['created_at', 'updated_at', 'completion_percentage']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'created_by')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'completed')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
        ('Statistics', {
            'fields': ('completion_percentage',),
            'classes': ('collapse',)
        }),
    )

    def is_overdue(self, obj):
        if obj.is_overdue:
            return format_html('<span style="color: red;">⚠️ Overdue</span>')
        return format_html('<span style="color: green;">✓ On Track</span>')
    is_overdue.short_description = 'Status'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'assigned_to', 'priority', 'due_date', 'completed', 'is_overdue']
    list_filter = ['completed', 'priority', 'due_date', 'created_at', 'assigned_to', 'project']
    search_fields = ['title', 'description', 'project__name', 'assigned_to__username']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['priority', 'due_date', 'created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'project', 'assigned_to')
        }),
        ('Status & Priority', {
            'fields': ('completed', 'priority', 'due_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def is_overdue(self, obj):
        if obj.is_overdue:
            return format_html('<span style="color: red;">⚠️ Overdue</span>')
        return format_html('<span style="color: green;">✓ On Track</span>')
    is_overdue.short_description = 'Status'
