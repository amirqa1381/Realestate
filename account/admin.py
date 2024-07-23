from django.contrib import admin

# Register your models here.
from .models import User, RealEstate


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    fieldsets = [
        (
            None,
            {'fields': ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'address']},
        ),
        (
            'Advanced Option',
            {
                "classes": ["collapse"],
                "fields": ["city", "country", "phone", "image"],
            }
        )
    ]


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    list_display = ['ceo', 'is_guarantee', 'city', 'country']
