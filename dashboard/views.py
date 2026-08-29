"""
Foydalanuvchi Dashboard'i: mening e'lonlarim, sevimlilar, chatlar, profil
bittalik joyda jamlanadi.
"""
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from chat.models import Conversation
from favorites.models import Favorite
from properties.models import Property


@login_required
def dashboard_view(request):
    """Foydalanuvchining shaxsiy boshqaruv paneli."""
    my_properties = Property.objects.filter(owner=request.user).order_by('-created_at')
    my_favorites = Favorite.objects.filter(user=request.user).select_related('property')[:6]
    my_conversations = Conversation.objects.filter(
        Q(buyer=request.user) | Q(seller=request.user)
    ).select_related('listing')[:6]

    context = {
        'my_properties': my_properties,
        'my_favorites': my_favorites,
        'my_conversations': my_conversations,
        'properties_count': my_properties.count(),
        'favorites_count': Favorite.objects.filter(user=request.user).count(),
    }
    return render(request, 'dashboard/dashboard.html', context)
