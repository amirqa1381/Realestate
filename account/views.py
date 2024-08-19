from django.shortcuts import render, redirect
import logging
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView
from .forms import (RegistrationForm,
                    LoginForm,
                    ContactForm,
                    UserChangeInfoForm,
                    UserPasswordChangeForm,
WorkProfileInfoForm
                    )
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

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


class UserPanelView(LoginRequiredMixin, TemplateView):
    """
    this class is for a moment that user want to fo to the accounts page and see its info or maybe
    he/she wants to change some info , so we should make a page for himself/herself when wants to do that
    and here i want to use the TemplateView for showing the template to the user
    """
    template_name = 'account/user_panel.html'


class UserChangeInfoView(LoginRequiredMixin, FormView):
    """
    this class is for a time that user wants to insert or change some information of it
    so when user wants to edit some of that information can go this route and handle that
    """
    form_class = UserChangeInfoForm
    template_name = 'account/user_info.html'
    success_url = reverse_lazy('user_info')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """
        this class is for the changing password and when a user know the current password and wants
        to change it  , can go to this page and change the current password, but when forgot the password should
        try another way and go to the forgotten password and change it
    """
    form_class = UserPasswordChangeForm
    template_name = 'account/changing_password.html'
    success_url = reverse_lazy('user_panel')


class WorkProfileInfoView(LoginRequiredMixin, FormView):
    """
    this class is for implementing the view for getting the work info and decision of the user for
    inserting the advertisement to the system
    """
    form_class = WorkProfileInfoForm
    template_name = 'account/user_profile_for_work.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return super().form_valid(form)
