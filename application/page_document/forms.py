from django import forms
from django.forms import ModelForm
from application.models import (
    Document,
)

class DocumentForm(forms.ModelForm):
    # file = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),)
    class Meta:
        model = Document
        fields = [
            'series_no',
            'description',
            'category',
            'year',
            'file',
            'remarks',
        ]
