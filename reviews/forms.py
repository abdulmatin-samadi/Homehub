"""Sharh qoldirish formasi."""
from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """Foydalanuvchi e'longa baho va sharh qoldirishi uchun forma."""

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3,
                'placeholder': "Fikringizni yozing...",
            }),
        }
        labels = {
            'rating': "Baho",
            'comment': "Sharh",
        }
