from django import forms
from .models import Mechanic, Repair, RepairImages, MechanicRequestForRepair
from django.forms import modelformset_factory

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
        


class RepairForm(forms.ModelForm):
    """
    this is the class that i have and it's for the repairing 
    """
    class Meta:
        model = Repair
        fields = ['issue']
        widgets = {
            'issue': forms.Textarea(attrs={'class': 'form-control'}),
        }
        


class RepairImagesForm(forms.ModelForm):
    """
    this class is for adding the form images and handling the images for it
    """
    class Meta: 
        model = RepairImages
        fields = ['images', 'alt']
        widgets = {
            'images': forms.FileInput(attrs={'class': 'form-control'}),
            'alt': forms.TextInput(attrs={'class': 'form-control'})
        }
        

RepairImagesFormset = modelformset_factory(RepairImages, form=RepairImagesForm, extra=2, can_delete=True)



class MechanicRequestForm(forms.ModelForm):
    """
    this class is for the handling the sending the request for the repairing the home
    """
    class Meta:
        model = MechanicRequestForRepair
        fields = ['start_time', 'end_time', 'repair_requirements']
        widgets = {
            'start_time': forms.DateInput(attrs={'class': 'form-control'}),
            'end_time': forms.DateInput(attrs={'class': 'form-control'}),
            'repair_requirements': forms.Textarea(attrs={'class': 'form-control'}),
        }