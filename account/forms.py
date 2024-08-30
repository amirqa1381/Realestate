from django import forms
from django.contrib.auth.forms import (UserCreationForm,
                                       AuthenticationForm,
                                       UserChangeForm,
                                       PasswordChangeForm,
                                       )
from account.models import User, Contact, ProfileOfSellerOrRealEstate, Agent


class RegistrationForm(UserCreationForm):
    """
    this class is for user registration and here we inherit from the UserCreationForm that
    was defined in the django by default for normal usage
    """
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password',
                                required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                label='Confirmation Password', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False


class LoginForm(AuthenticationForm):
    """
    this form is for authentication the user and inherit from the Authentication class
    that is in the built-in classes of the django
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password',
                               required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class ContactForm(forms.ModelForm):
    """
    this class is for the contact form and this form is a way for contacting between the
    user and site owners
    """

    class Meta:
        model = Contact
        fields = ['subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'})
        }
        labels = {
            'subject': '',
            'message': ''
        }


class UserChangeInfoForm(UserChangeForm):
    """
    this class is for that when user wants or should complete or edit some info in the django
    here this form handel that for it and we should provide a form for it for editing the information of
    that
    """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'city', 'country', 'phone', 'image']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(UserChangeInfoForm, self).__init__(*args, **kwargs)
        # we can remove the password field with pop the password from the fields
        # self.fields.pop('password')

        self.fields = {field_name: self.fields[field_name] for field_name in self.fields if field_name != 'password'}


class UserPasswordChangeForm(PasswordChangeForm):
    """
    this class is for the changing the user password
    """
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                   label='Current Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                    label='New Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                    label='Confirm New Password')


class WorkProfileInfoForm(forms.ModelForm):
    """
    this class is for the form that get the user work info and save to the database
    each user that wants to add advertisement to the site should fill this form
    """

    class Meta:
        model = ProfileOfSellerOrRealEstate
        fields = ['job_description', 'home_phone', 'birth_year', 'owner_or_agent']

        widgets = {
            'job_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert your Job....'}),
            'home_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_year': forms.DateInput(attrs={'class': 'form-control'}),
            'owner_or_agent': forms.Select(attrs={'class': 'form-select'})
        }


class AgentRegistration(forms.ModelForm):
    """
    this is the class that is for the registration and here we create new agent when they register
    """

    class Meta:
        model = Agent
        fields = ['working_history', 'working_year_number', 'realEstate']
        widgets = {
            'working_history': forms.Textarea(attrs={'class': 'form-control'}),
            'working_year_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'realEstate': forms.Select(attrs={'class': 'form-select'}),
        }
