from django import forms
from django.db.models import fields

from krypniteweb.models import Wishlist

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = "__all__"