from django.contrib import admin

from .models import OrderCheckout

class OrderCheckoutAdmin(admin.ModelAdmin):
    list_display = ['__str__','billing_profile']
    class Meta:
        model = OrderCheckout

admin.site.register(OrderCheckout, OrderCheckoutAdmin)