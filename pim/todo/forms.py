from django.forms import ModelForm
from .models import Task
# Create the form class.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        