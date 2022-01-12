from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


# Register your models here.
class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-start_date',)
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'is_restaurant_manager')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_restaurant_manager')
        }),
    )


admin.site.register(NewUser, UserAdminConfig)
