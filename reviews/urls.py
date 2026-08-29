"""reviews app uchun URL marshrutlari."""
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('<int:pk>/qoshish/', views.add_review_view, name='add_review'),
]
