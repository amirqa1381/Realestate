from django.forms.formsets import ManagementForm
from django.shortcuts import render, redirect
import logging
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth.views import LoginView
from .forms import (RegistrationForm,
                    LoginForm,
                    ContactForm,
                    UserChangeInfoForm,
                    UserPasswordChangeForm,
                    WorkProfileInfoForm,
                    AgentRegistration
                    )
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from main.models import Home, HomeImages
from main.forms import HomeForm, HomeImageFormSet

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
        form.completed = True
        form.save()
        return super().form_valid(form)


class AgentRegistrationView(LoginRequiredMixin, FormView):
    """
    this class is for a time that user is an agent and want to work in the site and work as agent in the site,
    and we choose the agent for ourselves from these users
    """
    form_class = AgentRegistration
    template_name = 'account/agent_registration.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.agent = self.request.user
        instance.is_active = True
        instance.save()
        return super().form_valid(form)


class UserRegisterProperty(LoginRequiredMixin, ListView):
    """
    this class is for showing the list of all property that user registered
    """
    template_name = "account/user_property.html"

    def get_queryset(self):
        return self.request.user.home.all()


class EditInfoOfUserProperty(LoginRequiredMixin, View):
    """
    this is a class that we have and its for modifying of the homes that current user registered
    """

    def get(self, request: HttpRequest, slug):
        """
        this is the get method, and it's for handling the get request that user sent to the endpoint
        """
        home_instance = Home.objects.get(owner=request.user, slug=slug)
        form = HomeForm(instance=home_instance)
        context = {
            'form': form,
            'home_instance': home_instance
        }
        return render(request, 'account/edit_user_property_page.html', context)

    def post(self, request: HttpRequest, slug):
        """
        this is the post method, and it's for a time that user will change something in the database or change something
        """
        home_instance = Home.objects.get(owner=request.user, slug=slug)
        form = HomeForm(request.POST, instance=home_instance)
        if form.is_valid():
            home = form.save(commit=False)
            home.owner = request.user
            home.is_active = True
            home.save()
            return redirect('edit_user_property', slug=slug)
        else:
            context = {
                'form': form,
                'home_instance': home_instance,
            }
            return render(request, 'account/edit_user_property_page.html', context)
