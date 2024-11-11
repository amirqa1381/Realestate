from django.urls import path
from .views import BorrowerRegisterView


urlpatterns = [
    path("borrower-register/", BorrowerRegisterView.as_view(), name='borrower_register'),
]
