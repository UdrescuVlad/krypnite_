from django.db import models

from billing_app.models import BillingProfile
import billing_app

COUNTRY_SHIPPING = (
    ('ro', 'Romania'),
)

ADDRESS_TYPE = (
    ('shipping','Shipping'),
    ('billing','Billing'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, null=True, blank=True, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=8, default="shipping", choices=ADDRESS_TYPE)
    primary_address = models.CharField(max_length=200)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default="ro", choices=COUNTRY_SHIPPING)
    state_province = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{primary_address}\n{city}\n{state_province}\n{country}\n{postal_code}".format(
            primary_address = self.primary_address,
            city = self.city,
            state_province = self.state_province,
            country = self.country,
            postal_code = self.postal_code
        )