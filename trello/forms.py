from django import forms
from .models import Task


class TaskListForm(forms.Form):
    name = forms.CharField(max_length=50)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime_local'})
        }
