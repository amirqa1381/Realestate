from django.shortcuts import render
from django.http import HttpRequest
from django.views import View
from .models import Home
from account.models import Agent
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


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
