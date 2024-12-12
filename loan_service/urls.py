from django.urls import path
from .views import (BorrowerRegisterView,
                    CheckingActivateCode,
                    LoanServiceView,
                    WalletView,
                    WalletDepositView,
                    )


urlpatterns = [
    path("borrower-register/", BorrowerRegisterView.as_view(), name='borrower_register'),
    path("checking-activate-code/", CheckingActivateCode.as_view(), name="checking_activate_code"),
    path("loan-service/", LoanServiceView.as_view(), name="loan_service"),
    path("wallet/", WalletView.as_view(), name="wallet"),
    path("deposit/", WalletDepositView.as_view(), name="wallet_deposit")
]
