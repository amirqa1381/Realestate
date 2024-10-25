from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MechanicalRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages


class MechanicRegister(LoginRequiredMixin, FormView):
    """
    this class is for registering the mechanic user for working as mechanic 
    """
    form_class = MechanicalRegistrationForm
    template_name = 'repair/mechanical_register.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.is_active = True
        form.save()
        messages.success(self.request, "The id is registered SUCCESSFULLY")
        return super().form_valid(form)
    
