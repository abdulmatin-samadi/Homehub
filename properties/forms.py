"""
E'lon (Property) qo'shish/tahrirlash formasi va qo'shimcha rasmlar uchun
inline formset.
"""
from django import forms
from django.forms import inlineformset_factory

from .models import Property, PropertyImage


class PropertyForm(forms.ModelForm):
    """E'lon yaratish/tahrirlash uchun asosiy forma."""

    class Meta:
        model = Property
        fields = [
            'title', 'description', 'price',
            'region', 'district', 'address',
            'area', 'rooms', 'floor', 'year_built',
            'condition', 'deal_type', 'main_image',
            'latitude', 'longitude',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Masalan: 3 xonali quyosh kvartira"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': "E'lon haqida batafsil yozing..."}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Narxni so'mda kiriting"}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Tuman nomi"}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ko'cha, uy raqami"}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Masalan: 65.5"}),
            'rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor': forms.NumberInput(attrs={'class': 'form-control'}),
            'year_built': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Masalan: 2020"}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'deal_type': forms.Select(attrs={'class': 'form-control'}),
            'main_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Masalan: 41.311081", 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Masalan: 69.240562", 'step': 'any'}),
        }
        labels = {
            'title': "Sarlavha",
            'description': "Tavsif",
            'price': "Narx (so'm)",
            'region': "Viloyat",
            'district': "Tuman",
            'address': "Manzil",
            'area': "Maydon (m²)",
            'rooms': "Xonalar soni",
            'floor': "Qavat",
            'year_built': "Qurilgan yil",
            'condition': "Holati",
            'deal_type': "Bitim turi",
            'main_image': "Asosiy rasm",
            'latitude': "Kenglik (ixtiyoriy, xarita uchun)",
            'longitude': "Uzunlik (ixtiyoriy, xarita uchun)",
        }

    def clean_price(self):
        """Narx musbat son ekanligini tekshiradi."""
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Narx musbat son bo'lishi kerak.")
        return price


class PropertyImageForm(forms.ModelForm):
    """Bitta qo'shimcha rasm uchun forma (formset ichida ishlatiladi)."""

    class Meta:
        model = PropertyImage
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }


# E'lon bilan birga bir nechta qo'shimcha rasmni bitta formada yuklash uchun
PropertyImageFormSet = inlineformset_factory(
    Property,
    PropertyImage,
    form=PropertyImageForm,
    fields=['image'],
    extra=3,
    can_delete=True,
)
