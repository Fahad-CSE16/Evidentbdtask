from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    
    list_display = ['email','is_active', 'is_admin']
    list_filter = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password','is_active')}),
        ('Personal info', {'fields': ('first_name','last_name','gender','date_of_birth','blood_group','phone')}),
        ('Permissions', {'fields': ('is_admin','is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()

admin.site.register(User, UserAdmin)