from django import forms
from todo_list.models import TODOO

class TodoForm(forms.ModelForm):
    class Meta:
        model = TODOO
        fields = ['title', 'category']

    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )