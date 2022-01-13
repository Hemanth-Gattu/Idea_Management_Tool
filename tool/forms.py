from django import forms
from .models import Task

class NoteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','content','bucket')

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['bucket'].required = False
