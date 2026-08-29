"""Sevimlilarga qo'shish/olib tashlash va ro'yxatni ko'rsatish view'lari."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from properties.models import Property
from .models import Favorite


@login_required
def toggle_favorite_view(request, pk):
    """
    E'lonni sevimlilarga qo'shadi yoki (agar allaqachon qo'shilgan bo'lsa)
    olib tashlaydi. POST so'rovi orqali ishlaydi, so'ng ortga qaytaradi.
    """
    property_obj = get_object_or_404(Property, pk=pk)
    favorite, created = Favorite.objects.get_or_create(user=request.user, property=property_obj)

    if not created:
        favorite.delete()
        messages.info(request, "E'lon sevimlilardan olib tashlandi.")
    else:
        messages.success(request, "E'lon sevimlilarga qo'shildi.")

    next_url = request.POST.get('next') or property_obj.get_absolute_url()
    return redirect(next_url)


@login_required
def favorite_list_view(request):
    """Foydalanuvchining barcha sevimli e'lonlari ro'yxati."""
    favorites = Favorite.objects.filter(user=request.user).select_related('property', 'property__owner')
    return render(request, 'favorites/favorite_list.html', {'favorites': favorites})
