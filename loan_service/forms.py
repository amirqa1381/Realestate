from django import forms
from .models import Borrower, LoanService
from django.core.exceptions import ValidationError


class BorrowerForm(forms.ModelForm):
    """
    this class is for handling the form for the Borrower request and object
    """
    class Meta:
        model = Borrower
        fields = ['bank_account_number', 'bank', 'has_got_loan_service']
        widgets = {
            'bank_account_number': forms.NumberInput(attrs={'class':'form-controls', 'placeholder':'Only 12 digit'}),
            'bank': forms.Select(attrs={'class':'form-control'}),
            'has_got_loan_service': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style':'margin-left:15px'})
        }
        
    
    def clean_bank_account_number(self):
        number = self.cleaned_data.get('bank_account_number')
        if len(str(number)) > 12:
            raise ValidationError("The bank account number cannot exceed 12 digits.")
        return number


class ActivateCodeCheckingForm(forms.Form):
    """
    this class was for the checking that user insert correct activate code or not
    """
    activate_code = forms.IntegerField(label="Activate Code", min_value=1000000, max_value=20000000, widget=forms.NumberInput(attrs={'class':'form-control'}))


class LoanServiceForm(forms.ModelForm):
    """
    this class is for handling the form and page of sending request of lending and if the borrower has conditions of loans 
    can get the loan and it will active for it
    """
    class Meta:
        model = LoanService
        fields = ['price', 'refund_month']