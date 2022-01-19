from django.db import models

from cart_app.models import Cart
#TUPLE -> STANGA: CE SE SCRIE IN DB(store value), DREAPTA: CE SE AFISEAZA(display value)
ORDER_STATUS = (
    ('created', 'Created'),
    ('payed', 'Payed'),
    ('shipping_in_progress', 'Shipping in progress'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'), # a restitui bani
    ('returned', 'Returned'), # a returna produsul
)

class OrderCheckout(models.Model):
    order_id = models.CharField(max_length=200, blank=True)
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='created', choices=ORDER_STATUS)
    shipping_total = models.DecimalField(default=1.99, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id

#   generate order id
#   generate order total