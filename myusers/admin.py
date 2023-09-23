from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Roles

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'phone_number')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone_number',  'first_name', 'last_name', 'email', 'phone_number', 'is_active', 'is_staff', 'groups', 'user_permissions'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
