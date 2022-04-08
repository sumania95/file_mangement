from django import forms
from django.forms import ModelForm
from application.models import (
    Ordinance_Resolution_Document,
)

class Ordinance_Resolution_DocumentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),)
    remarks = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),required=False)

    class Meta:
        model = Ordinance_Resolution_Document
        fields = [
            'document_number',
            'description',
            'category',
            'remarks',
            'file',
            'date_approved',
        ]
