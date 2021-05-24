from django.contrib import admin
from .models import Task, Project

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_on')
    list_filter = ("status", 'project')
    search_fields = ['title', 'description']

admin.site.register(Task, PostAdmin)
admin.site.register(Project)