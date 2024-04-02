from django.utils import timezone

from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = ["title", "content", "deadline", "tags"]

        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
