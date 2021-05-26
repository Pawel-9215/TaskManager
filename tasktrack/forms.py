from django import forms
from django.forms import widgets
from tasktrack.models import Task, Project

class ProjectForm(forms.ModelForm):

    class Meta():
        model = Project
        fields = ('owner', 'title', 'status')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
        }

class TaskForm(forms.ModelForm):

    class Meta():
        model = Task
        fields = {'author', 'project', 'title', 'description', 'status'}

        widgets = {
                'title': forms.TextInput(attrs={'class':'textinputclass'}),
                'description': forms.TextInput(attrs={'class':'textinputclass'}),
            }