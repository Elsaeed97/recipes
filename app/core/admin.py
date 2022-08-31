"""
    Customize Django Admin
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """Define the Admin Pages for users"""
    ordering = ['id']
    list_display = ['id', 'name', 'email']
    fieldsets = (
        (None, {
            "fields": (
                ('email', 'password')
            ),
        }),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )

            }
        ),
        (
            _('Important Dates'),
            {
                'fields':
                    ('last_login',),
            }
        )
    )
    readonly_fields = ['last_login']
