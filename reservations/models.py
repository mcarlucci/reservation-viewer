from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=150)
    phone = models.IntegerField(max_length=15, blank=True)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

