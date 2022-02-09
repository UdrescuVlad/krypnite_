from django import forms
from krypniteweb.models import Product

class ProductForm(forms.ModelForm):
    
    
    #   https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#selecting-the-fields-to-use
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['slug']
        