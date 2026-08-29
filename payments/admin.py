from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Admin to'lov holatini o'zgartirib, e'lonni premium qila oladi."""
    list_display = ('property', 'user', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)
    search_fields = ('property__title', 'user__username')
