"""
Ko'chmas mulk e'loni (Property) va uning qo'shimcha rasmlari (PropertyImage)
modellari.
"""
from django.conf import settings
from django.db import models
from django.urls import reverse

from pages.constants import UZ_REGIONS


def property_main_image_path(instance, filename):
    """Har bir e'lon uchun asosiy rasmni alohida papkaga saqlaydi."""
    return f'properties/{instance.pk or "temp"}/main/{filename}'


def property_extra_image_path(instance, filename):
    """E'lonning qo'shimcha rasmlarini alohida papkaga saqlaydi."""
    return f'properties/{instance.property_id}/extra/{filename}'


class Property(models.Model):
    """Ko'chmas mulk e'loni: uy, kvartira, yer va h.k."""

    class DealType(models.TextChoices):
        """E'lon turi: sotiladi yoki ijaraga beriladi."""
        SALE = 'sale', "Sotiladi"
        RENT = 'rent', "Ijaraga"

    class Condition(models.TextChoices):
        """Mulkning joriy holati."""
        NEW = 'new', "Yangi qurilgan"
        GOOD = 'good', "Yaxshi holatda"
        NEEDS_REPAIR = 'repair', "Ta'mir talab qiladi"

    # ---- Asosiy ma'lumotlar ----
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    price = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Narx (so'm)")

    # ---- Manzil ----
    region = models.CharField(max_length=30, choices=UZ_REGIONS, verbose_name="Viloyat")
    district = models.CharField(max_length=100, verbose_name="Tuman")
    address = models.CharField(max_length=255, verbose_name="Aniq manzil")

    # ---- Xususiyatlar ----
    area = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Maydon (m²)")
    rooms = models.PositiveSmallIntegerField(verbose_name="Xonalar soni")
    floor = models.PositiveSmallIntegerField(verbose_name="Qavat")
    year_built = models.PositiveSmallIntegerField(verbose_name="Qurilgan yil")
    condition = models.CharField(max_length=10, choices=Condition.choices, default=Condition.GOOD, verbose_name="Holati")
    deal_type = models.CharField(max_length=4, choices=DealType.choices, verbose_name="Bitim turi")

    # ---- Xarita (ixtiyoriy) ----
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="Kenglik (latitude)")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="Uzunlik (longitude)")

    # ---- Rasmlar ----
    main_image = models.ImageField(upload_to=property_main_image_path, verbose_name="Asosiy rasm")

    # ---- Egasi va holat ----
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name="Egasi",
    )
    is_active = models.BooleanField(default=True, verbose_name="Faol (saytda ko'rinadi)")
    is_premium = models.BooleanField(default=False, verbose_name="Premium e'lon")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """E'lon tafsilotlari sahifasiga havola (Detail View uchun)."""
        return reverse('properties:property_detail', kwargs={'pk': self.pk})


class PropertyImage(models.Model):
    """Bitta e'longa tegishli qo'shimcha rasmlar (galereya)."""

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="E'lon",
    )
    image = models.ImageField(upload_to=property_extra_image_path, verbose_name="Rasm")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Qo'shimcha rasm"
        verbose_name_plural = "Qo'shimcha rasmlar"

    def __str__(self):
        return f"{self.property.title} - rasm #{self.pk}"
