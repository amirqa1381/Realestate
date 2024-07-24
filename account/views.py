from django.shortcuts import render
import logging
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, LoginForm
from django.urls import reverse_lazy


logger = logging.getLogger(__name__)


class UserRegistrationView(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('index')
    template_name = 'account/register.html'

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    """
    this class is allowed us that login the user inside the service
    """
    authentication_form = LoginForm
    template_name = 'account/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        logger.info(f"User {form.cleaned_data['username']} logged in successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning(f"Failed login attempt for user {form.cleaned_data['username']}")
        return super().form_invalid(form)
