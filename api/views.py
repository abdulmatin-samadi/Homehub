"""Property uchun REST API (DRF ViewSet)."""
from rest_framework import permissions, viewsets

from properties.models import Property
from .serializers import PropertySerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Faqat egasi o'zgartirish/o'chirish huquqiga ega, boshqalar faqat o'qiy oladi."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class PropertyViewSet(viewsets.ModelViewSet):
    """
    E'lonlar uchun to'liq REST API:
    GET /api/properties/        - ro'yxat
    POST /api/properties/       - yangi e'lon (login talab qilinadi)
    GET /api/properties/{id}/   - tafsilot
    PUT/PATCH /api/properties/{id}/ - tahrirlash (faqat egasi)
    DELETE /api/properties/{id}/    - o'chirish (faqat egasi)
    """
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Property.objects.filter(is_active=True).select_related('owner').prefetch_related('images')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
