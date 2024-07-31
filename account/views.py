from django.shortcuts import render, redirect
import logging
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, LoginForm, ContactForm
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin

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


class ContactView(LoginRequiredMixin, View):
    """
    this class is for the contact form, and we should use the FormView, but I decided to use
    the View for writing this view and I think it's good practice for doing it.
    """

    def get(self, request: HttpRequest):
        """
        this is function for handling the get request that comes to the view and rout that we defined
        """
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'account/contact.html', context)

    def post(self, request: HttpRequest):
        """
        this is the function that we wrote, and it's responsible for the post method and it handel the
        requests that come to this view.
        """
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'account/contact.html', context)
