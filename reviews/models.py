"""E'lonlarga yoziladigan sharh va baho (5 yulduzli) modeli."""
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from properties.models import Property


class Review(models.Model):
    """Foydalanuvchi tomonidan e'longa yoziladigan sharh va baho."""

    RATING_CHOICES = [(i, f"{i} yulduz") for i in range(1, 6)]

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="E'lon",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Foydalanuvchi",
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Baho",
    )
    comment = models.TextField(max_length=1000, verbose_name="Sharh")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yozilgan sana")

    class Meta:
        verbose_name = "Sharh"
        verbose_name_plural = "Sharhlar"
        # Bir foydalanuvchi bitta e'longa faqat bitta sharh yoza oladi
        unique_together = ('property', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.property} ({self.rating}★)"
