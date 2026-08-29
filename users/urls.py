"""users app uchun URL marshrutlari."""
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/avatar/', views.avatar_upload_view, name='avatar_upload'),
    path('password/change/', views.UserPasswordChangeView.as_view(), name='password_change'),
]
