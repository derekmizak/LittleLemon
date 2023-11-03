from rest_framework import serializers
from .models import Menu, Booking
from django.utils import timezone


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    def validate_price(self, value):
        """
        Check that the price is greater than or equal to zero.
        """
        if value < 0:
            raise serializers.ValidationError("Price must be greater than or equal to zero.")
        return value

    def validate_inventory(self, value):
        """
        Check that the inventory is greater than or equal to zero.
        """
        if value < 0:
            raise serializers.ValidationError("Inventory must be greater than or equal to zero.")
        return value


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate_no_of_guests(self, value):
        """
        Check that the number of guests is greater than zero.
        """
        if value < 0:
            raise serializers.ValidationError("Number of guests must be greater than zero.")
        return value

    def validate_date(self, value):
        """
        Check that the date is in the future.
        """
        
        if value < timezone.now():
            raise serializers.ValidationError("Date must be in the future.")
        return value



