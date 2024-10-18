from django import forms
from .models import Topic


class Topic_form(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name', 'description', 'duration', 'course']
