from django import forms
from .models import Mechanic

class MechanicalRegistrationForm(forms.ModelForm):
    """
    this class is for the registration of the mechanic user 
    """
    class Meta:
        model = Mechanic
        fields = ['mechanical_engineering_code']
        widgets = {
            'mechanical_engineering_code': forms.TextInput(attrs={'class':'form-control','placeholder':'The length should be 12 character'}),
        }    