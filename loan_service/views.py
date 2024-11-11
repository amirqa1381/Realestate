from django.shortcuts import render
from django.views.generic import FormView
from .forms import BorrowerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages



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
        form = form.save(commit=False)
        form.user = self.request.user
        form.is_active = True
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Form submission failed. Please correct the following errors:")
        for field , errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return response
 
    
    
    