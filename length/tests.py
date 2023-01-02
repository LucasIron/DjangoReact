from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestLengthConversion(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('length:DjangoReact')

    def test_centimeter_to_meter_conversion(self):
        data = {
            'input_unit': 'centimeter',
            'output_unit': 'meter',
            'input_value': round(8096.894, 3)
        }

        response = self.client.get(self.url, data)

        self.assertContains(response, 80.969)