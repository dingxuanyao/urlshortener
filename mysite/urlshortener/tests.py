from django.test import TestCase
from .models import Url


class UrlTestCase(TestCase):
    def setUp(self):
        url = Url(full_url="https://testdomain.net")
        url.save()

    def test_short_id_correct_length(self):
        """Verify short ID is 5 characters in length"""
        url = Url.objects.get(full_url="https://testdomain.net")
        self.assertEqual(len(url.short_id), 5)
