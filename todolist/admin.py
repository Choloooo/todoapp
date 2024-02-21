from django.contrib import admin
from .models import TodoItem

# Register your models here.
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title',  'completed', 'created_at')  # Fields to display in the admin list view
    list_filter = ('completed',)  # Filtering options in the admin list view
    search_fields = ('title', 'description')  # Search functionality in the admin list view

# Register the TodoItem model with the custom admin options
admin.site.register(TodoItem, TodoItemAdmin)
