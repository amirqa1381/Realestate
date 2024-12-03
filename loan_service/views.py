from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import BorrowerForm, ActivateCodeCheckingForm, LoanServiceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
from django.core.exceptions import ValidationError
from django.views import View
from django.http import HttpRequest


def create_activate_code():
    """
    this function is for creating the activate code and it's for handling it, 
    here we create a activate code and send it to the user and it should insert it to the 
    page that it redirect
    """
    random_number = random.randint(1000000, 20000000)
    return random_number


class BorrowerRegisterView(LoginRequiredMixin, FormView):
    """
    this class is for the handling the view of the register request of the borrower and we can handle it
    """
    form_class = BorrowerForm
    template_name = 'loan_service/borrower_register.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        """
        this method is for a time that a form is valid and we want to handle the s.th after validation the form.
        """
        activate_code = create_activate_code()
        form = form.save(commit=False)
        form.user = self.request.user
        form.is_active = True
        # here i want to fill the activate code for filling it
        form.activate_code = activate_code
        form.save()
        messages.success(self.request, "The info was saved successfully")
        # here is for sending the mail to user , and we send activate code to user for inserting it 
        # and if it does not provide the activate code that we provide it , it can not go to the next step
        send_mail("Activate Code", f"{activate_code}", settings.EMAIL_HOST_USER, [self.request.user.email,], fail_silently=False)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Form submission failed. Please correct the following errors:")
        for field , errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return response
 
    
    


class CheckingActivateCode(LoginRequiredMixin, FormView):
    """
    in this class we check that user insert correct activate code and if it insert correct one we can redirect it to the new page 
    and if it does not provide correct code it show to us that it is not correct user and we should take attention to it
    """
    form_class = ActivateCodeCheckingForm
    template_name = 'loan_service/activate_code_checking.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        """
        this method is for checking the validation of the form 
        """
        # here we check that current user has been registered as borrower
        if hasattr(self.request.user, 'borrower') and self.request.user.borrower:
            a_code = self.request.user.borrower.activate_code
        else:
            messages.error(self.request, "You should first register as borrower")
        
        # here we retrieve the input activate code
        activate_code = form.cleaned_data['activate_code']
        # check the activate code
        if activate_code == a_code:
            messages.success(self.request, "The activation code was successfully gotten")
            return super().form_valid(form)
        else:
            messages.error(self.request, "The activation code was incorrect")
            return super().form_invalid(form)
        
        
class LoanServiceView(LoginRequiredMixin, FormView):
    """
    this class is for the handling the lending to the user and throw this class , user will send loan request to the user
    """
    form_class = LoanServiceForm
    template_name = 'loan_service/Loan_service.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        loan_service = form.save(commit=False)
        # here i have check the that user has submitted a form for registering the borrower 
        if hasattr(self.request.user, 'borrower'):
            loan_service.borrower = self.request.user.borrower
        else:
            messages.error(self.request, "This user has not registered as a Borrower , You should first fill that part and after that you can return to this page")
            return redirect('borrower_register')
        try:
            # here i have set the loan service and handle that 
            loan_service.save()
            messages.success(self.request, 'Loan request submitted successfully....')
            return super().form_valid(form)
        except ValidationError as e:
            for error in e.messages:
                messages.error(self.request, error)
            
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Form submission failed. Please correct the following errors:")
        for field , errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return response



class WalletView(LoginRequiredMixin, View):
    """
    this class is for handling the view of the wallet and it's for get and post of that 
    """
    def get(self, request:HttpRequest):
        """
        this is the get method that i have and it's handle the get method
        """
        return render(self.request, "loan_service/wallet.html")
    
    
    def post(self, request:HttpRequest):
        """
        this is the get method that i have and it's handle the get method
        """
        pass