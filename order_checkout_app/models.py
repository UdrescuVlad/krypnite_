from decimal import Decimal
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_random_order_id
from cart_app.models import Cart

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
    
    def update_total(self):
        self.total = self.cart.total + float(Decimal(self.shipping_total))
        self.save()
        return self.total
    
    class Meta:
        unique_together = ('order_id','cart')
    #   https://www.queworx.com/django/django-get_or_create/

#   generate order id - random and unique 
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    #   daca nu am un order id, creeaza-mi unul
    if not instance.order_id:
        instance.order_id = unique_random_order_id(instance)

pre_save.connect(pre_save_create_order_id, sender=OrderCheckout)


#   generate order total
def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = OrderCheckout.objects.filter(cart__id = cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total, sender=Cart)

def post_save_order(sender, instance, created, *args, **kwargs):
    print("running")
    if created:
        print("updating first...")
        instance.update_total()

post_save.connect(post_save_order, sender=OrderCheckout)

# post_save -> right after the model is saved
# pre_save -> right before the model is saved