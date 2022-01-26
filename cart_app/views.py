from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from billing_app.models import BillingProfile
from .models import Cart, cart_pre_save_receiver
from order_checkout_app.models import OrderCheckout
from krypniteweb.models import Product, product_pre_save_receiver
from django.contrib.auth.decorators import login_required

# @login_required
def cart_home(request):
    cart, new_obj = Cart.objects.new_or_get(request)
    return render(request, "home.html", {'cart':cart})

# @login_required
def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("It happens that the product is not found! We're sorry.\n\tWe will refund you with one month for free!")
            redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)

        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['no_of_items']=cart_obj.products.count()
    return redirect("cart:home")

def checkout_redirect(request):
    cart_obj, new_cart = Cart.objects.new_or_get(request)
    if new_cart or cart_obj.products.count() == 0:
        return redirect("cart:home")

    
    billing_profile = None
    if request.user.is_authenticated:
        billing_profile,billing_profile_created = BillingProfile.objects.get_or_create(user=request.user,email=request.user.email)
    else:
        pass
    
    #   ar trebui sa ne asiguram ca nu ca esxista un singur cos
    #   de cumparaturi pe acest order, de aceea am creat 
    #   field-ul de "active"

    one_cart_qs = OrderCheckout.object.filter(cart=cart_obj, active=True)
    if one_cart_qs.exists():
        one_cart_qs.update(active=False)
    else:
        order_obj, created = OrderCheckout.objects.create(cart=cart_obj, billing_profile=billing_profile)

    context={
        'order': order_obj,
        'billing_profile': billing_profile
    }

    return render(request, "checkout.html", context)