from django.urls import path
from .views import MechanicRegister



urlpatterns = [
    path("register-mechanic/", MechanicRegister.as_view(), name="mechanic_register"),
]
