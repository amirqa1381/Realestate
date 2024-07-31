from django.urls import path
from .views import UserRegistrationView, UserLoginView, ContactView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('contact/', ContactView.as_view(), name='contact'),
]
