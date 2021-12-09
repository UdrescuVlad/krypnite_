from django.db import models
from django.conf import settings
from krypniteweb.models import Product
from django.db.models.signals import pre_save,m2m_changed

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        query = self.get_queryset().filter(id=cart_id)
        if query.count() == 1:
            new_obj = False
            cart_object = query.first()
            if request.user.is_authenticated and cart_object.user is None:
                cart_object.user = request.user
                cart_object.save()
        else:
            cart_object = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_object.id
        return cart_object, new_obj

    def new(self, user=None):
        user_object = None
        if user is not None:
            if user.is_authenticated:
                user_object = user
        return self.model.objects.create(user=user_object)

User = settings.AUTH_USER_MODEL
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

def cart_m2m_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products_cart = instance.products.all()
        total=0

        for product in products_cart:
            total = total + product.price
        
        instance.subtotal = total
        
        instance.save()
m2m_changed.connect(cart_m2m_receiver, sender=Cart.products.through)

#   I want that total to be also updated
def cart_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.total != instance.subtotal:
        instance.total = instance.subtotal
pre_save.connect(cart_pre_save_receiver, sender=Cart)
