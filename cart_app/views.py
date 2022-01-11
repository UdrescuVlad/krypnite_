from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Cart, cart_pre_save_receiver
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
            print("It happens the product is not found! We're sorry.\n\tWe will refund you with one month for free!")
            redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)

        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['no_of_items']=cart_obj.products.count()
    return redirect("cart:home")