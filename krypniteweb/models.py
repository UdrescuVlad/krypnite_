from django.db import models
from django.db.models.fields import EmailField
from django.core.validators import RegexValidator

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=200)
    product_photo = models.ImageField(null=True, blank=True, upload_to="images/")

class Wishlist(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    phone_regex = RegexValidator(regex=r'^\+{1}40\d{9}$', message="Phone number must be entered in the format: '+40123456789'. Up to 12 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    description = models.TextField(max_length=200)
    estimation_time = models.DecimalField(max_digits=6, decimal_places=2)