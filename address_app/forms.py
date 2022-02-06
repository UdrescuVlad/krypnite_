from django import forms

from .models import Address

class AddressForm(forms.ModelForm):
    #   https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#selecting-the-fields-to-use
    class Meta:
        model = Address
        fields = "__all__"
        exclude = ["billing_profile","address_type"]
        