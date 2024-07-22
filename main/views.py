from django.shortcuts import render
from django.http import HttpRequest
from django.views import View


class IndexView(View):
    """
    this class view is for showing the page that is the main page,
    and we render the properties in this page
    """

    def get(self, request: HttpRequest):
        """
        this method is for the get method and it handel the get method request
        """
        return render(request, 'main/index.html')

    def post(self, request: HttpRequest):
        """
        this method is for the post method and it handel the post method request
        """
        pass
