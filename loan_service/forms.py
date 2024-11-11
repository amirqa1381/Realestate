from django import forms
from .models import Borrower


class BorrowerForm(forms.ModelForm):
    """
    this class is for handling the form for the Borrower request and object
    """
    class Meta:
        model = Borrower
        fields = ['bank_account_number', 'bank', 'has_got_loan_service']
        widgets = {
            'bank_account_number': forms.NumberInput(attrs={'class':'form-controls'}),
            'bank': forms.Select(attrs={'class':'form-control'}),
            'has_got_loan_service': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }