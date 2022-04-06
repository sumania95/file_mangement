from django import forms
from django.forms import ModelForm
from application.models import (
    Year,
)

class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = [
            'year',
        ]
