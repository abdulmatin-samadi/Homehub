"""
Autentifikatsiya va profil bilan bog'liq view'lar:
Register, Login, Logout, Profile, Avatar yuklash, Parolni almashtirish.
"""
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .forms import RegisterForm, UserLoginForm, ProfileUpdateForm, AvatarUploadForm


def register_view(request):
    """Yangi foydalanuvchini ro'yxatdan o'tkazadi va avtomatik login qiladi."""
    if request.user.is_authenticated:
        return redirect('users:profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Xush kelibsiz, {user.first_name or user.username}! Ro'yxatdan muvaffaqiyatli o'tdingiz.")
            return redirect('users:profile')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    """Foydalanuvchini tizimga kiritadi."""
    if request.user.is_authenticated:
        return redirect('users:profile')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Muvaffaqiyatli tizimga kirdingiz.")
                next_url = request.GET.get('next')
                return redirect(next_url or 'users:profile')
            messages.error(request, "Foydalanuvchi nomi yoki parol noto'g'ri.")
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


@login_required
def logout_view(request):
    """Foydalanuvchini tizimdan chiqaradi."""
    logout(request)
    messages.info(request, "Siz tizimdan chiqdingiz.")
    return redirect('pages:home')


@login_required
def profile_view(request):
    """Profil sahifasi: ma'lumotlarni ko'rish va tahrirlash."""
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil ma'lumotlari yangilandi.")
            return redirect('users:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    avatar_form = AvatarUploadForm(instance=request.user)
    return render(request, 'users/profile.html', {
        'form': form,
        'avatar_form': avatar_form,
    })


@login_required
def avatar_upload_view(request):
    """Faqat profil rasmini (avatar) yuklash uchun alohida endpoint."""
    if request.method == 'POST':
        avatar_form = AvatarUploadForm(request.POST, request.FILES, instance=request.user)
        if avatar_form.is_valid():
            avatar_form.save()
            messages.success(request, "Profil rasmi yangilandi.")
        else:
            messages.error(request, "Rasm yuklashda xatolik yuz berdi.")
    return redirect('users:profile')


class UserPasswordChangeView(PasswordChangeView):
    """
    Django'ning tayyor PasswordChangeView'idan foydalanamiz -
    parolni xavfsiz almashtirish logikasini qayta yozish shart emas.
    """
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Parol o'zgargandan keyin sessiya bekor bo'lmasligi uchun
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, "Parolingiz muvaffaqiyatli almashtirildi.")
        return response
