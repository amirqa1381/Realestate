from django import forms
from .models import PropertyRequest, Home, HomeImages
from django.forms import modelformset_factory


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


class HomeImagesForm(forms.ModelForm):
    """
    this is for the images of the homes and each home can have multiple images
    """

    class Meta:
        model = HomeImages
        fields = ['image', 'alt']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'alt': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PropertySellForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['address', 'meter', 'city', 'country', 'postal_code', 'price', 'description', 'floor', 'beds',
                  'baths', 'garages', 'year_built']

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'meter': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'floor': forms.NumberInput(attrs={'class': 'form-control'}),
            'beds': forms.NumberInput(attrs={'class': 'form-control'}),
            'baths': forms.NumberInput(attrs={'class': 'form-control'}),
            'garages': forms.NumberInput(attrs={'class': 'form-control'}),
            'year_built': forms.DateInput(attrs={'class': 'form-control'}),
        }


HomeImageFormSet = modelformset_factory(HomeImages, form=HomeImagesForm, extra=1, can_delete=True, min_num=1, max_num=10)
