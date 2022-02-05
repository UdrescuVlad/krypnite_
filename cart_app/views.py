from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from billing_app.models import BillingProfile
from .models import Cart, FavouriteList, cart_pre_save_receiver
from order_checkout_app.models import OrderCheckout
from krypniteweb.models import Product, product_pre_save_receiver
from django.contrib.auth.decorators import login_required

# @login_required
def cart_home(request):
    cart, new_obj = Cart.objects.new_or_get(request)
    print('cartobj:')
    print(cart)
    return render(request, "home.html", {'cart':cart})

# @login_required
def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            redirect("krypnite:products")
        cart_obj, new_obj = Cart.objects.new_or_get(request)

        #   sync-async - mai este produsul in cos?
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['no_of_items']=cart_obj.products.count()
    return redirect("cart:home")

def fav_list_home(request):
    favlist, new_favlist = FavouriteList.objects.new_or_get(request)
    print('favlist_obj:')
    print(favlist)
    return render(request, "favourite_list.html", {'favlist':favlist})

def fav_list_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            redirect("krypnite:products")
        fav_list_obj, new_fav_list_obj = FavouriteList.objects.new_or_get(request)

        if product_obj in fav_list_obj.products.all():
            fav_list_obj.products.remove(product_obj)
        else:
            fav_list_obj.products.add(product_obj)
        request.session['no_fav_list_items'] = fav_list_obj.products.count()
    return redirect("cart:favhome")

def checkout_redirect(request):
    cart_obj, new_cart = Cart.objects.new_or_get(request)
    order_obj = None
    if new_cart or cart_obj.products.count() == 0:
        return redirect("cart:home")
    billing_profile = None
    if request.user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=request.user,email=request.user.email)
    else:
        redirect("krypnite:login")

    if billing_profile is not None:
        # order_obj, order_obj_created = OrderCheckout.objects.new_or_get(billing_profile, order_obj)
        qs = OrderCheckout.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        if qs.count() == 1:
            order_obj = qs.first()
        else:
            #   am adaugat urm 3 linii la presave cart
            # old_order = OrderCheckout.objects.exclude(billing_profile=billing_profile).filter(cart=cart_obj, active=True)
            # if old_order.exists():
            #     old_order.update(active = False)
            order_obj = OrderCheckout.objects.create(billing_profile=billing_profile, cart=cart_obj)
    context={
        'order': order_obj,
        'billing_profile': billing_profile
    }
    return render(request, "checkout.html", context)