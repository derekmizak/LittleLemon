from django.db import models


# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    no_of_guests = models.IntegerField()
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title

    