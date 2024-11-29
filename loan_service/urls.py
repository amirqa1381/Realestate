from django.urls import path
from .views import BorrowerRegisterView, CheckingActivateCode, LoanServiceView


urlpatterns = [
    path("borrower-register/", BorrowerRegisterView.as_view(), name='borrower_register'),
    path("checking-activate-code/", CheckingActivateCode.as_view(), name="checking_activate_code"),
    path("loan-service/", LoanServiceView.as_view(), name="loan_service")
]
