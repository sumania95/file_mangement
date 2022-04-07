from django import forms
from django.forms import ModelForm
from application.models import (
    Order_Document,
)

class Order_DocumentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),)
    remarks = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),required=False)

    class Meta:
        model = Order_Document
        fields = [
            'document_number',
            'description',
            'order_category',
            'remarks',
            'file',
            'date_signed',
        ]
