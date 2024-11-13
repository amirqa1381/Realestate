from django.shortcuts import render
from django.views.generic import FormView
from .forms import BorrowerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random



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
 
    
    
    