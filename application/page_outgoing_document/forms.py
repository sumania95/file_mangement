from django import forms
from django.forms import ModelForm
from application.models import (
    Outgoing_Document,
)

class Outgoing_DocumentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),)
    remarks = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),required=False)
    
    class Meta:
        model = Outgoing_Document
        fields = [
            'description',
            'outgoing_category',
            'remarks',
            'file',
            'date_issued',
        ]
