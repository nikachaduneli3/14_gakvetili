from django.db import models


class ProductTypes(models.TextChoices):
    DAIRY = 'dairy', 'Dairy'
    DRINKS = 'drink', 'Drinks'
    MEAT = 'meat', 'Meat'
    COMEULI = 'com', 'Comeuli'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    qty = models.IntegerField(default=0)
    type = models.CharField(max_length=100, choices=ProductTypes)
