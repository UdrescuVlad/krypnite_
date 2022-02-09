from django import forms
from krypniteweb.models import Product
from order_checkout_app.models import OrderCheckout


class ProductForm(forms.ModelForm):
    
    #   https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#selecting-the-fields-to-use
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['slug']


class OrderCheckoutForm(forms.ModelForm):

    def clean_order_ext_id(self):
        order_ext_id = self.cleaned_data.get("order_ext_id")
        return order_ext_id

    def clean_status(self):
        status = self.cleaned_data.get("status")
        return status

    class Meta:
        model = OrderCheckout
        fields = ['order_ext_id', 'status']
        exclude = []
        widgets = {
            'order_ext_id': forms.TextInput,
            'status': forms.Select,
        }