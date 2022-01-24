from django import forms
from django.db.models import fields
from django.contrib.auth import get_user_model
from django.forms import widgets
from krypniteweb.models import Wishlist, RegistrationModel

User = get_user_model()

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = "__all__"

class RegistrationModelForm(forms.ModelForm):
    def clean_name(self):
        username = self.cleaned_data.get("name")
        query_set = User.objects.filter(username = username)
        if query_set.exists():
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        query_set = User.objects.filter(email = email)
        if query_set.exists():
            raise forms.ValidationError("Email is already registered.")
        return email

    class Meta:
        model = RegistrationModel
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }