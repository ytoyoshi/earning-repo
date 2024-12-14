from django import forms
from django.forms import ModelForm

from .models import TodoModel

class DateInput(forms.DateInput):
    input_type = "date"

class TodoForm(ModelForm):

    class Meta:
        model = TodoModel
        fields = ('title','memo','priority','deadline')
        widgets = {
            'deadline': DateInput(),
        }