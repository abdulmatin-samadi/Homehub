"""Foydalanuvchining sevimli e'lonlari (Like/Favorite) modeli."""
from django.conf import settings
from django.db import models

from properties.models import Property


class Favorite(models.Model):
    """Foydalanuvchi va e'lon o'rtasidagi 'sevimli' bog'lanishi."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name="Foydalanuvchi",
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='favorited_by',
        verbose_name="E'lon",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")

    class Meta:
        verbose_name = "Sevimli e'lon"
        verbose_name_plural = "Sevimli e'lonlar"
        # Bir foydalanuvchi bitta e'lonni faqat bir marta sevimlilarga qo'sha oladi
        unique_together = ('user', 'property')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} → {self.property}"
