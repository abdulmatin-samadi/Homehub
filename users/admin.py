"""Admin panelda foydalanuvchilarni boshqarish sozlamalari."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom User modelini admin panelda to'g'ri ko'rsatish uchun."""

    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'is_staff', 'created_at')
    list_filter = ('role', 'is_staff', 'is_active', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')
    ordering = ('-date_joined',)

    # Standart UserAdmin fieldsets'iga qo'shimcha maydonlarni qo'shamiz
    fieldsets = UserAdmin.fieldsets + (
        ("Qo'shimcha ma'lumotlar", {'fields': ('phone_number', 'avatar', 'role', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Qo'shimcha ma'lumotlar", {'fields': ('email', 'phone_number', 'role')}),
    )
