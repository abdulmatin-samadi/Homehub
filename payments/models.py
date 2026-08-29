"""
To'lovlar (Payments) app'i.

DIQQAT: Bu yerda haqiqiy to'lov tizimi (Payme, Click va h.k.) ulanmagan,
chunki bu API kalitlari va shartnoma talab qiladi. Hozircha "Premium
e'lon" xizmati uchun to'lov SO'ROVI yaratiladi, so'ng admin uni
tasdiqlab, e'lonni premium qilib belgilaydi. Bu - keyinchalik haqiqiy
to'lov shlyuzi ulanadigan tayyor infratuzilma.
"""
from django.conf import settings
from django.db import models

from properties.models import Property


class Payment(models.Model):
    """Premium e'lon xizmati uchun to'lov so'rovi/yozuvi."""

    class Status(models.TextChoices):
        PENDING = 'pending', "Kutilmoqda"
        CONFIRMED = 'confirmed', "Tasdiqlangan"
        REJECTED = 'rejected', "Rad etilgan"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name="Foydalanuvchi",
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name="E'lon",
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Summa (so'm)")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "To'lov"
        verbose_name_plural = "To'lovlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.property} - {self.amount} so'm ({self.get_status_display()})"

    def save(self, *args, **kwargs):
        """To'lov tasdiqlanganda e'lonni avtomatik premium qiladi."""
        super().save(*args, **kwargs)
        if self.status == self.Status.CONFIRMED and not self.property.is_premium:
            self.property.is_premium = True
            self.property.save(update_fields=['is_premium'])
