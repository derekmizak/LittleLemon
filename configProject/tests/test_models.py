from rest_framework.test import APITestCase
from rest_framework import status
from restaurant.models import Menu
from django.test import TestCase


class MenuTest(TestCase):
    def test_get_menu(self):
        """
        Ensure we can get a menu item.
        """
        menu_item = Menu.objects.create(title='Chicken', price=100, description='Fried Chicken', inventory=10)
        self.assertEqual(menu_item.title, 'Chicken')