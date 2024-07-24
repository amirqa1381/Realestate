from django.contrib import admin
from .models import Home, Rent, Repair, Sell, HomeImages


class HomeImageInlineAdmin(admin.TabularInline):
    model = HomeImages
    extra = 1


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    """
    this class is for the home model, and it created for showing the fields of the home in the admin page
    """
    list_display = ['owner', 'make_address_shorter', 'meter', 'is_active']
    list_filter = ['meter', 'city', 'country', 'is_active']
    inlines = [HomeImageInlineAdmin,]


admin.site.register(Rent)
admin.site.register(Repair)
admin.site.register(Sell)
