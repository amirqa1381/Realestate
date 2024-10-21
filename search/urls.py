from django.urls import path
from .views import search_func

urlpatterns = [
    path("", search_func, name="search"),
]
