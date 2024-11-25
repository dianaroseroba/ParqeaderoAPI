from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('parqueadero', 'direccion', 'telefono'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {
            'classes': ('wide',),
            'fields': ('parqueadero', 'direccion', 'telefono'),
            }),
        )