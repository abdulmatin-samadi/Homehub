"""
Foydalanuvchi modeli.

Django'ning standart User modeli o'rniga custom model ishlatamiz, chunki
keyingi qadamlarda telefon raqami, avatar va rol (sotuvchi/xaridor) kabi
maydonlar kerak bo'ladi. Buni loyiha boshida qilish - Django Best Practice.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


def avatar_upload_path(instance, filename):
    """Har bir foydalanuvchi avatari uchun alohida papka yaratadi."""
    return f'avatars/user_{instance.pk}/{filename}'


class User(AbstractUser):
    """
    Standart AbstractUser'ni kengaytiruvchi custom foydalanuvchi modeli.
    username, email, password kabi maydonlar AbstractUser'dan keladi.
    """

    class Role(models.TextChoices):
        """Foydalanuvchi turi: oddiy foydalanuvchi yoki mulk egasi."""
        BUYER = 'buyer', "Xaridor"
        SELLER = 'seller', "Sotuvchi / Egasi"

    phone_regex_help = "Telefon raqamini quyidagi formatda kiriting: '+998901234567'"

    phone_number = models.CharField(
        max_length=13,
        blank=True,
        verbose_name="Telefon raqami",
        help_text=phone_regex_help,
    )
    avatar = models.ImageField(
        upload_to=avatar_upload_path,
        blank=True,
        null=True,
        verbose_name="Profil rasmi",
    )
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.BUYER,
        verbose_name="Foydalanuvchi turi",
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="O'zi haqida",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan sana")

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ['-date_joined']

    def __str__(self):
        return self.get_full_name() or self.username

    @property
    def avatar_url(self):
        """Avatar mavjud bo'lmasa standart rasm URL'ini qaytaradi."""
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return '/static/img/default-avatar.png'
