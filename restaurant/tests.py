from rest_framework.test import APITestCase
from rest_framework import status
from .models import Menu

class MenuAPITestCase(APITestCase):
    def test_create_menu_item_with_negative_price(self):
        """
        Ensure we can't create a menu item with a negative price.
        """
        url = '/menu/'
        data = {'title': 'Test Item', 'price': -10, 'description': 'Test', 'inventory': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Menu.objects.count(), 0)
