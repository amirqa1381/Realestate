from django.shortcuts import render
from django.views.generic import FormView
from .forms import RegistrationForm
from django.urls import reverse_lazy


class UserRegistrationView(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('index')
    template_name = 'account/register.html'
    
    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
