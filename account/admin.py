from django.contrib import admin

# Register your models here.
from .models import User, RealEstate, Agent, ProfileOfSellerOrRealEstate


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    fieldsets = [
        (
            None,
            {'fields': ['username', 'password', 'email', 'first_name', 'last_name', 'is_active', 'is_staff',
                        'address']},
        ),
        (
            'Advanced Option',
            {
                "classes": ["collapse"],
                "fields": ["city", "country", "phone", "image"],
            }
        )
    ]

    def has_add_permission(self, request):
        """
        in this function we set that only the superuser can add new user in the database
        """
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_change_permission(self, request, obj=None):
        """
        in the change function all the staff and superuser can change the user information
        """
        return True


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    list_display = ['ceo', 'is_guarantee', 'city', 'country']


admin.site.register(Agent)
admin.site.register(ProfileOfSellerOrRealEstate)