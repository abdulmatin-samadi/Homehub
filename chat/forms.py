"""Chat uchun xabar yuborish formasi."""
from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    """Suhbat ichida yangi xabar yozish uchun forma."""

    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 2,
                'placeholder': "Xabar yozing...",
            }),
        }
        labels = {'text': ''}
