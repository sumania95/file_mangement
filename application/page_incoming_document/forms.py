from django import forms
from django.forms import ModelForm
from application.models import (
    Incoming_Document,
)

class Incoming_DocumentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),)
    remarks = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),required=False)
    class Meta:
        model = Incoming_Document
        fields = [
            'description',
            'incoming_category',
            'file',
            'remarks',
            'date_received',
        ]
