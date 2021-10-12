from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=200)