from django.contrib import admin 
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')  # Define the fields to display
    search_fields= ('task',)

admin.site.register(Task,TaskAdmin)