"""Django REST Framework serializerlari (hozircha Property uchun)."""
from rest_framework import serializers

from properties.models import Property, PropertyImage


class PropertyImageSerializer(serializers.ModelSerializer):
    """Qo'shimcha rasmlar uchun serializer."""

    class Meta:
        model = PropertyImage
        fields = ['id', 'image']


class PropertySerializer(serializers.ModelSerializer):
    """E'lonlar ro'yxati va tafsilotlari uchun serializer."""

    owner = serializers.StringRelatedField(read_only=True)
    images = PropertyImageSerializer(many=True, read_only=True)
    region_display = serializers.CharField(source='get_region_display', read_only=True)
    deal_type_display = serializers.CharField(source='get_deal_type_display', read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'price',
            'region', 'region_display', 'district', 'address',
            'area', 'rooms', 'floor', 'year_built', 'condition',
            'deal_type', 'deal_type_display',
            'main_image', 'images', 'owner',
            'is_active', 'is_premium', 'created_at',
        ]
        read_only_fields = ['id', 'owner', 'created_at']
