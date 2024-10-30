from django.urls import path
from .views import MechanicRegister, RepairChoosingHouse



urlpatterns = [
    path("register-mechanic/", MechanicRegister.as_view(), name="mechanic_register"),
    path("repair-choosing-house/", RepairChoosingHouse.as_view(), name="home_choosing_house"),
]
