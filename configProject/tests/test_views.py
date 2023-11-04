from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking
from restaurant.views import MenuItemView, SingleMenuItemView, BookingViewSet
from restaurant.serializers import MenuSerializer, BookingsSerializer


class MenuItemViewTests(APITestCase):
    def setUp(self):
        # Set up data for the tests
        Menu.objects.create(title="Test Item", price=9.99, description="Test Description", inventory=10)

    def test_list_menu_items(self):
        # Test retrieving a list of menu items
        url = reverse('menu')  # Update with the actual name of the URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_menu_item(self):
        url = reverse('menu')  # Update with the actual name of the URL
        data = {'title': "New Item", 'price': 12.99, 'description': "New Description", 'inventory': 10}
        response = self.client.post(url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)  # This will print the validation errors if any
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SingleMenuItemViewTests(APITestCase):
    def setUp(self):
        # Set up data for the tests
        self.menu_item = Menu.objects.create(title="Test Item", price=9.99, description="Test Description", inventory=10)

    def test_retrieve_menu_item(self):
        # Test retrieving a single menu item
        url = reverse('menu-item', args=[self.menu_item.id])  # Update with the actual name of the URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.menu_item.title)

    def test_update_menu_item(self):
        # Test updating a menu item
        url = reverse('menu-item', args=[self.menu_item.id])  # Update with the actual name of the URL
        data = {'title': "Updated Item", 'price': 10.99, 'description': "Updated Description", 'inventory': 10}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_menu_item(self):
        # Test deleting a menu item
        url = reverse('menu-item', args=[self.menu_item.id])  # Update with the actual name of the URL
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookingViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.booking = Booking.objects.create(
            name='Test Booking',
            date=datetime.now(),
            no_of_guests=4
        )
        self.url = reverse('booking-list')  # Make sure 'booking-list' is the correct name in your URL conf

    