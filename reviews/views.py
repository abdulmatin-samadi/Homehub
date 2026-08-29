"""Sharh qo'shish view'i (property detail sahifasidagi forma orqali ishlaydi)."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from properties.models import Property
from .forms import ReviewForm
from .models import Review


@login_required
def add_review_view(request, pk):
    """E'longa yangi sharh va baho qo'shadi. Bir foydalanuvchi - bitta sharh."""
    property_obj = get_object_or_404(Property, pk=pk)

    if Review.objects.filter(property=property_obj, user=request.user).exists():
        messages.warning(request, "Siz bu e'longa allaqachon sharh qoldirgansiz.")
        return redirect(property_obj.get_absolute_url())

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.property = property_obj
            review.user = request.user
            review.save()
            messages.success(request, "Sharhingiz uchun rahmat!")
        else:
            messages.error(request, "Sharh yuborishda xatolik yuz berdi.")

    return redirect(property_obj.get_absolute_url())
