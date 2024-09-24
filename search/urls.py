from django.urls import path
from .views import serach_func

urlpatterns = [
    path("", serach_func, name="search"),
]
