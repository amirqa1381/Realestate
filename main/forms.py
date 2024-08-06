from django import forms
from .models import PropertyRequest


class PropertyRequestForm(forms.ModelForm):
    class Meta:
        model = PropertyRequest
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }
        labels = {
            'name': '',
            'email': '',
            'message': ''
        }
