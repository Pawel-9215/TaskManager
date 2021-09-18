from django import forms
from django.forms import widgets
from tasktrack.models import Task, Project

class ProjectForm(forms.ModelForm):

    class Meta():
        model = Project
        fields = ('title', 'status')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
        }

class TaskForm(forms.ModelForm):

    class Meta():
        model = Task
        fields = {'project', 'title', 'description', 'deadline_in', 'status'}

        widgets = {
                'title': forms.TextInput(attrs={'class':'textinputclass'}),
                'description': forms.Textarea(attrs={'class':'textinputclass-description'}),
                'deadline_in': forms.SelectDateWidget(attrs={'class':'textinputclass'}),
            }
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(owner=self.request.user)