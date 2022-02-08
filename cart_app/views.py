from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from address_app.forms import AddressForm
from address_app.models import Address

from billing_app.models import BillingProfile
from .models import Cart, FavouriteList, cart_pre_save_receiver
from order_checkout_app.models import OrderCheckout
from krypniteweb.models import Product, product_pre_save_receiver
from django.contrib.auth.decorators import login_required
from krypniteweb.templates import *


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

    shipping_billing_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)
    query_address = None
    billing_profile = None
    if request.user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=request.user,email=request.user.email)
    else:
        redirect("krypnite:login")

    if billing_profile is not None:
        query_address = Address.objects.filter(billing_profile = billing_profile)


        order_obj, order_obj_created = OrderCheckout.objects.new_or_get(billing_profile, cart_obj)

        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        elif billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()
    
    if request.method == 'POST':
        is_client_fill_bill = order_obj.is_client_fill_bill_data()
        print(is_client_fill_bill)
        if is_client_fill_bill:
            status_order = order_obj.order_status_payed()
            print(status_order)
            request.session['no_of_items'] = 0
            del request.session['cart_id']
            return render(request, "checkout_done.html", {"order": order_obj})

    context={
        'order': order_obj,
        'billing_profile': billing_profile,
        'form': shipping_billing_form,
        'addresses': query_address
    }
    return render(request, "checkout.html", context)


def checkout_paid(request):
    return render(request, "checkout_done.html", {})

