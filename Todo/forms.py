from django import forms

from Todo.models import Task


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
        )
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
