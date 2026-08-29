"""favorites app uchun URL marshrutlari."""
from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('', views.favorite_list_view, name='favorite_list'),
    path('<int:pk>/toggle/', views.toggle_favorite_view, name='toggle_favorite'),
]
