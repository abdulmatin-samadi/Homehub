"""
Xaridor va sotuvchi o'rtasidagi sayt ichi yozishmalar (chat) modellari.

Eslatma: bu real-time (WebSocket) chat emas - oddiy sahifa yangilanishi
(HTTP so'rov) asosida ishlaydigan Django chat. Real-time uchun kelajakda
Django Channels qo'shilishi mumkin.
"""
from django.conf import settings
from django.db import models

from properties.models import Property


class Conversation(models.Model):
    """Bitta e'lon bo'yicha xaridor va sotuvchi o'rtasidagi suhbat."""

    listing = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='conversations',
        verbose_name="E'lon",
    )
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='conversations_as_buyer',
        verbose_name="Xaridor",
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='conversations_as_seller',
        verbose_name="Sotuvchi",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Suhbat"
        verbose_name_plural = "Suhbatlar"
        # Bitta e'lon bo'yicha bir xaridor-sotuvchi juftligi uchun bitta suhbat
        unique_together = ('listing', 'buyer', 'seller')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.buyer} ↔ {self.seller} ({self.listing})"

    @property
    def last_message(self):
        """Suhbatdagi eng oxirgi xabarni qaytaradi (ro'yxatda ko'rsatish uchun)."""
        return self.messages.order_by('-created_at').first()


class Message(models.Model):
    """Bitta suhbat ichidagi alohida xabar."""

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name="Suhbat",
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        verbose_name="Jo'natuvchi",
    )
    text = models.TextField(verbose_name="Matn")
    is_read = models.BooleanField(default=False, verbose_name="O'qilgan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        ordering = ['created_at']

    def __str__(self):
        return f"{self.sender}: {self.text[:30]}"
