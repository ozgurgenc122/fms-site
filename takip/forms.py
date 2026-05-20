from django import forms
from .models import Is


class IsForm(forms.ModelForm):
    class Meta:
        model = Is
        exclude = []