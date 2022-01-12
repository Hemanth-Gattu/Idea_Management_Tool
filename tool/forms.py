from django import forms
from .models import Task

class NoteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','content')

