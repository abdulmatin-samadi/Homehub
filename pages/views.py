"""
Bosh sahifa (Home Page) view'i.

DIQQAT: 'properties' app hali yaratilmagan (u 3-qadamda qo'shiladi).
Shuning uchun bu yerda Property modelini import qilishga urinamiz;
agar app hali mavjud bo'lmasa, bo'sh ro'yxat bilan ishlaymiz - bu sahifa
hech qanday xatosiz ishlaydi va 3-qadamdan keyin avtomatik ravishda
haqiqiy e'lonlarni ko'rsata boshlaydi.
"""
from django.apps import apps
from django.shortcuts import render

from .constants import UZ_REGIONS


def home_view(request):
    """Bosh sahifani premium va so'nggi e'lonlar bilan chiqaradi."""
    premium_properties = []
    latest_properties = []

    # 'properties' app o'rnatilgan bo'lsa, haqiqiy e'lonlarni yuklaymiz.
    # Hozircha (2-qadamda) bu app mavjud emas, shuning uchun bo'sh holatda
    # ishlaydi va sahifa hech qanday xatosiz ko'rsatiladi.
    if apps.is_installed('properties'):
        Property = apps.get_model('properties', 'Property')
        premium_properties = Property.objects.filter(
            is_active=True, is_premium=True
        ).select_related('owner')[:6]
        latest_properties = Property.objects.filter(
            is_active=True
        ).select_related('owner').order_by('-created_at')[:8]

    context = {
        'premium_properties': premium_properties,
        'latest_properties': latest_properties,
        'regions': UZ_REGIONS,
    }
    return render(request, 'pages/home.html', context)
