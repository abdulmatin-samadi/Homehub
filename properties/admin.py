"""Admin panelda e'lonlarni boshqarish sozlamalari."""
from django.contrib import admin

from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    """E'lon tahrirlash sahifasida qo'shimcha rasmlarni birga ko'rsatish."""
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """E'lonlarni admin panelda boshqarish."""

    list_display = ('title', 'owner', 'region', 'deal_type', 'price', 'is_active', 'is_premium', 'created_at')
    list_filter = ('deal_type', 'region', 'condition', 'is_active', 'is_premium')
    search_fields = ('title', 'description', 'address', 'district')
    list_editable = ('is_active', 'is_premium')
    inlines = [PropertyImageInline]
    date_hierarchy = 'created_at'


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    """Qo'shimcha rasmlarni alohida ham boshqarish imkoniyati."""
    list_display = ('property', 'uploaded_at')
