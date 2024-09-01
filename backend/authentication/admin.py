from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address')}),
    )
    list_display = ['username', 'email', 'phone_number', 'address', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
