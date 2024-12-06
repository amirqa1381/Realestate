from django.contrib import admin
from .models import  Wallet, LoanService



@admin.register(Wallet)
class AdminWallet(admin.ModelAdmin):
    """
    this class is for the bring the wallet to the admin page , and we can create the wallet for each user
    """
    list_display = ['user', 'balance', 'created_at']




admin.site.register(LoanService)
