from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from properties.models import Property
from pages.constants import UZ_REGIONS


class PropertyModelTests(TestCase):
    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="testuser",
            password="TestPass123!"
        )

        self.property = Property.objects.create(
            title="Test uy",
            description="Test tavsif",
            price="250000000.00",
            region=UZ_REGIONS[0][0],
            district="Test tuman",
            address="Test manzil",
            area="80.00",
            rooms=3,
            floor=2,
            year_built=2020,
            deal_type=Property.DealType.SALE,
            main_image="test.jpg",
            owner=self.user,
        )

    def test_property_string_is_title(self):
        self.assertEqual(str(self.property), "Test uy")

    def test_property_get_absolute_url(self):
        expected_url = reverse(
            "properties:property_detail",
            kwargs={"pk": self.property.pk}
        )

        self.assertEqual(self.property.get_absolute_url(), expected_url)
