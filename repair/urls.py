from django.urls import path
from .views import MechanicRegister, RepairChoosingHouse, RepairSubmitView



urlpatterns = [
    path("register-mechanic/", MechanicRegister.as_view(), name="mechanic_register"),
    path("repair-choosing-house/", RepairChoosingHouse.as_view(), name="home_choosing_house"),
    path("repair-submit-request/<int:pk>/", RepairSubmitView.as_view(), name="repair_submit_view")
]
