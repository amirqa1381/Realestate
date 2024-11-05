from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (MechanicalRegistrationForm,
                    RepairForm,
                    RepairImagesFormset,
                    RepairImages,
                    MechanicRequestForm,
                    )

from django.urls import reverse_lazy
from django.contrib import messages
from main.models import Home
from django.views import View
from django.http import HttpRequest
from django.forms.formsets import ManagementForm
from .models import Repair


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
    
    

class RepairSubmitView(LoginRequiredMixin, View):
    """
    this class is for the submitting the repair request
    """
    def get(self, request: HttpRequest, pk):
        """
        this method is for handling the get method when the get request is coming to this view
        """
        home = Home.objects.get(pk=pk)
        form = RepairForm()
        form_set = RepairImagesFormset(queryset=RepairImages.objects.none(), prefix="repair_images")
        context = {
            'form': form,
            'form_set': form_set,
            'home': home
        }
        return render(request, "repair/repair_submit_view.html", context)
    
    def post(self, request:HttpRequest, pk):
        """
        this method is for handling the post method when the post request is coming to this view
        """
        # here i have retrieved the home that user wants to send the request for repairing
        home = Home.objects.get(pk=pk)
        form = RepairForm(request.POST)
        form_set = RepairImagesFormset(request.POST, request.FILES, prefix="repair_images")
        form_set.management_form = ManagementForm(request.POST, prefix="repair_images")
        # here we check that form and formset are valid or not
        if form.is_valid() and form_set.is_valid():
            repair = form.save(commit=False)
            repair.home = home
            repair.save()
            # here i have set the images that we have
            instances = form_set.save(commit=False)
            for instance in instances:
                instance.repair = repair
                instance.save()
            return redirect("index")
        else:
            context = {
            'form': form,
            'form_set': form_set
            }
            return render(request, "repair/repair_submit_view.html", context)
            
            
    
    
    
class RepairRequestList(LoginRequiredMixin, ListView):
    """
    this class is for the repair request lists, and we show the list of the all the repairs requests
    """ 
    model = Repair
    context_object_name = "repairs"
    template_name = "repair/repairs_list.html"
    
    
    
class MechanicRequestView(LoginRequiredMixin, FormView):
    """
    this is the class that is for submitting the mechanic request and handle that 
    """
    form_class = MechanicRequestForm
    success_url = reverse_lazy("index")
    template_name = 'repair/mechanic_request.html'
    
    def get_object(self):
        """
        this method is for retrieving the object from the url
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(Repair, pk=pk)
    
    def get_context_data(self, **kwargs):
        """
        this method is for handling the context in the template
        """
        context = super().get_context_data(**kwargs)
        context['repair'] = self.get_object()
        return context
    
    
    def form_valid(self, form):
        """
        this method is for handling the process of validation of the form 
        """
        form = form.save(commit=False)
        form.mechanic = self.request.user.mechanic
        form.repair = self.get_object()
        form.save()        
        return super().form_valid(form)

    
    
    
    