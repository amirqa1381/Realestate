from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MechanicalRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages
from main.models import Home


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
    


class RepairChoosingHouse(LoginRequiredMixin, ListView):
    """
    this class is for choosing the houses that user registered
    """
    model = Home
    template_name = "repair/repair_homes_list.html"
    context_object_name = "homes"
    
    def get_queryset(self):
        """
        this function is for the filtering the homes that user registered in the site
        """
        return Home.objects.filter(owner = self.request.user)