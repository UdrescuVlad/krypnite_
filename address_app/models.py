from django.db import models

from billing_app.models import BillingProfile
import billing_app

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, null=True, blank=True, on_delete=models.CASCADE)
    primary_address = models.CharField(max_length=120)
    secondary_address = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default="Romania")
    state_province = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)