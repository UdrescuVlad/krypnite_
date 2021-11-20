from django import forms
from django.db.models import fields

from krypniteweb.models import Wishlist, RegistrationModel

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = "__all__"

class RegistrationModelForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields = "__all__"