"""
Chat view'lari:
- start_conversation_view: property detail sahifasidagi "Bog'lanish" tugmasi
  bosilganda xaridor-sotuvchi suhbatini yaratadi (yoki mavjudini topadi).
- conversation_list_view: foydalanuvchining barcha suhbatlari.
- conversation_detail_view: bitta suhbat ichidagi xabarlar va yangi xabar yozish.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from properties.models import Property
from .forms import MessageForm
from .models import Conversation


@login_required
def start_conversation_view(request, property_pk):
    """E'lon egasi bilan suhbatni boshlaydi (yoki mavjudiga o'tkazadi)."""
    property_obj = get_object_or_404(Property, pk=property_pk)

    if property_obj.owner == request.user:
        messages.warning(request, "O'zingizning e'loningizga xabar yubora olmaysiz.")
        return redirect(property_obj.get_absolute_url())

    conversation, _created = Conversation.objects.get_or_create(
        listing=property_obj,
        buyer=request.user,
        seller=property_obj.owner,
    )
    return redirect('chat:conversation_detail', pk=conversation.pk)


@login_required
def conversation_list_view(request):
    """Foydalanuvchi ishtirok etayotgan barcha suhbatlar ro'yxati."""
    conversations = Conversation.objects.filter(
        Q(buyer=request.user) | Q(seller=request.user)
    ).select_related('listing', 'buyer', 'seller')
    return render(request, 'chat/conversation_list.html', {'conversations': conversations})


@login_required
def conversation_detail_view(request, pk):
    """Bitta suhbat: barcha xabarlarni ko'rsatadi va yangisini yuborish imkonini beradi."""
    conversation = get_object_or_404(
        Conversation.objects.select_related('listing', 'buyer', 'seller'), pk=pk
    )

    # Faqat suhbat ishtirokchilari (xaridor yoki sotuvchi) kira oladi
    if request.user not in (conversation.buyer, conversation.seller):
        messages.error(request, "Bu suhbatni ko'rish huquqingiz yo'q.")
        return redirect('chat:conversation_list')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            return redirect('chat:conversation_detail', pk=conversation.pk)
    else:
        form = MessageForm()

    # Suhbatdoshning o'qilmagan xabarlarini o'qilgan deb belgilaymiz
    conversation.messages.exclude(sender=request.user).update(is_read=True)

    return render(request, 'chat/conversation_detail.html', {
        'conversation': conversation,
        'messages_list': conversation.messages.select_related('sender'),
        'form': form,
    })
