from django.urls import path
from .views import (UserRegistrationView,
                    UserLoginView,
                    ContactView,
                    UserPanelView,
                    UserChangeInfoView,
                    UserPasswordChangeView,
                    WorkProfileInfoView,
                    AgentRegistrationView,
                    UserRegisterProperty,
                    EditInfoOfUserProperty,
                    RealEstateRegistration,
                    UserLoanServiceListView,
                    )
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('user-panel/', UserPanelView.as_view(), name='user_panel'),
    path('user-info/', UserChangeInfoView.as_view(), name='user_info'),
    path('user-change-password/', UserPasswordChangeView.as_view(), name='user_change_password'),
    path('work-profile/', WorkProfileInfoView.as_view(), name='work_profile'),
    path('agent-register/', AgentRegistrationView.as_view(), name='agent_register'),
    path('user-register-property/', UserRegisterProperty.as_view(), name='user_register_property'),
    path('edit-user-property/<slug:slug>/', EditInfoOfUserProperty.as_view(), name='edit_user_property'),
    path('realestate-registration/', RealEstateRegistration.as_view(), name="realestate_register"),
    path('user-all-loan-services/', UserLoanServiceListView.as_view(), name='user_all_loan_services'),
]
