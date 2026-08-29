"""api app uchun URL marshrutlari - DRF router orqali avtomatik yaratiladi."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PropertyViewSet

router = DefaultRouter()
router.register('properties', PropertyViewSet, basename='api-property')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
