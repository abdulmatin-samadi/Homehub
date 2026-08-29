"""
Foydalanuvchi bilan bog'liq formalar: ro'yxatdan o'tish va profilni tahrirlash.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    """
    Ro'yxatdan o'tish formasi. Django'ning UserCreationForm'ini
    kengaytirib, email va telefon raqamini majburiy qilib qo'shamiz.
    """
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@mail.com',
        })
    )
    phone_number = forms.CharField(
        required=True,
        label="Telefon raqami",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+998901234567',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiya'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': "Foydalanuvchi nomi",
            'first_name': "Ism",
            'last_name': "Familiya",
            'role': "Siz kimsiz?",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Parol maydonlariga ham Bootstrap uslubini beramiz
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Parol'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Parolni takrorlang'})

    def clean_email(self):
        """Email allaqachon ro'yxatdan o'tganligini tekshiradi."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email allaqachon ro'yxatdan o'tgan.")
        return email


class UserLoginForm(forms.Form):
    """Tizimga kirish formasi (username yoki email orqali)."""
    username = forms.CharField(
        label="Foydalanuvchi nomi",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'})
    )
    password = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'})
    )


class ProfileUpdateForm(forms.ModelForm):
    """Profil ma'lumotlarini (ism, telefon, bio) tahrirlash formasi."""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'bio']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'first_name': "Ism",
            'last_name': "Familiya",
            'email': "Email",
            'phone_number': "Telefon raqami",
            'bio': "O'zi haqida",
        }


class AvatarUploadForm(forms.ModelForm):
    """Faqat profil rasmini yuklash uchun alohida forma."""

    class Meta:
        model = User
        fields = ['avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
        labels = {
            'avatar': "Profil rasmi",
        }
