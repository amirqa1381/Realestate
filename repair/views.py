from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MechanicalRegistrationForm, RepairForm, RepairImagesFormset, RepairImages
from django.urls import reverse_lazy
from django.contrib import messages
from main.models import Home
from django.views import View
from django.http import HttpRequest
from django.forms.formsets import ManagementForm


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
        form = RepairForm()
        form_sets = RepairImagesFormset(queryset=RepairImages.objects.none(), prefix="repair_images")
        context = {
            'form': form,
            'form_set': form_sets
        }
        return render(request, "repair/repair_submit_view.html", context)
    
    def post(self, request:HttpRequest, pk):
        """
        this method is for handling the post method when the post request is coming to this view
        """
        # here i have retrieved the home that user wants to send the request for repairing
        home = Home.objects.get(pk=pk)
        form = RepairForm(request.POST)
        form_sets = RepairImagesFormset(request.POST, request.FILES, prefix="repair_images")
        form_sets.management_form = ManagementForm(request.POST, prefix="repair_images")
        # here we check that form and formset are valid or not
        if form.is_valid() and form_sets.is_valid():
            repair = form.save(commit=False)
            repair.home = home
            repair.save()
            # here i have set the images that we have
            instances = form_sets.save(commit=False)
            for instance in instances:
                instance.repair = repair
                instance.save()
            return redirect("index")
        else:
            context = {
            'form': form,
            'form_set': form_sets
            }
            return render(request, "repair/repair_submit_view.html", context)
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    