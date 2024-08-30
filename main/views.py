from django.forms.formsets import ManagementForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.views import View
from .models import Home, Blog, HomeImages
from account.models import Agent
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PropertyRequestForm, HomeForm, HomeImageFormSet


class IndexView(View):
    """
    this class view is for showing the page that is the main page,
    and we render the properties in this page
    """

    def get(self, request: HttpRequest):
        """
        this method is for the get method and it handel the get method request
        """
        recently_homes = Home.objects.order_by('-created_at')[:6]
        agents = Agent.objects.all()[:6]
        context = {
            'recently_homes': recently_homes,
            'agents': agents,
        }
        return render(request, 'main/index.html', context)

    def post(self, request: HttpRequest):
        """
        this method is for the post method and it handel the post method request
        """
        pass


class AboutView(LoginRequiredMixin, TemplateView):
    """
    this class is for showing the about page to the user
    """
    template_name = 'main/about.html'


class BlogListView(LoginRequiredMixin, ListView):
    """
    this class is for showing the list of the Blogs
    """
    model = Blog
    template_name = 'main/blog.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        """
        here we make a query to the database for getting the latest books
        """
        return Blog.objects.all().order_by('-created_at')


class PropertyListView(LoginRequiredMixin, ListView):
    """
    this class is for showing the list of the properties in the page
    """
    model = Home
    template_name = 'main/property.html'
    context_object_name = 'properties'
    paginate_by = 6

    def get_queryset(self):
        return Home.objects.all().order_by('-created_at')


class SinglePropertyView(LoginRequiredMixin, View):
    """
    this class is for showing the all the information of the Property and connect the agent and customer
    together
    """

    def get(self, request: HttpRequest, slug):
        """
        this method is for the handling the get method of the view and when user sent a
        get request for getting all the info this view will work and handle that.
        """
        form = PropertyRequestForm()
        home = get_object_or_404(Home, slug=slug)
        context = {
            'home': home,
            'form': form,
        }
        return render(request, 'main/single_property.html', context)

    def post(self, request: HttpRequest, slug):
        """
        this method is for the handling the post method of the view and when user sent a
        post request for getting all the info this view will work and handle that.
        """
        form = PropertyRequestForm(request.POST)
        home = get_object_or_404(Home, slug=slug)
        if form.is_valid():
            submit = form.save(commit=False)
            submit.home = home
            submit.save()
            return redirect('single-property', slug=home.slug)
        context = {
            'home': home,
            'form': form,
        }
        return render(request, 'main/single_property.html', context)


class PropertySellView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        """
        this method is for the handling the get method that user send to the server, and we handle that request with
        this method
        """
        form = HomeForm()
        form_sets = HomeImageFormSet(queryset=HomeImages.objects.none(), prefix='home_images')
        context = {
            'form': form,
            'form_sets': form_sets,
        }
        return render(request, 'main/property_sell_page.html', context)

    def post(self, request: HttpRequest):
        form = HomeForm(request.POST)
        form_sets = HomeImageFormSet(request.POST, request.FILES, prefix="home_images")
        form_sets.management_form = ManagementForm(request.POST, prefix="home_images")
        print(form_sets.errors)
        print(form_sets.non_form_errors())
        print(form_sets.management_form.data)
        if form.is_valid() and form_sets.is_valid():  # Validate the formset as a whole
            home = form.save(commit=False)
            home.owner = request.user
            home.is_active = True
            home.save()
            instances = form_sets.save(commit=False)  # Get the instances from the formset
            for instance in instances:
                instance.home = home
                instance.save()
            return redirect('single-property', slug=home.slug)
        else:
            context = {
                'form': form,
                'form_sets': form_sets,
            }
            return render(request, 'main/property_sell_page.html', context)
