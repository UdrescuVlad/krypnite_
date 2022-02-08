from django.shortcuts import render

from django.shortcuts import render, redirect

from billing_app.models import BillingProfile
from order_checkout_app.models import OrderCheckout

def order_history(request):
    
    #   SA STIM BILLING PROFILE ID
    #   DUPA ACEST BILLING PROFILE , CAUTAM TOATE ORDERELE CARE AU ACEST BILLING PROFILE ID
    #   --------
    #   CE RETURNAM IN CONTEXT ? -> FOR PE ORDERE SI RETURNAM PENTRU FIECARE: ORDER_EXT_ID, CART.PRODUCTS, TOTAL, STATUS
    
    
    #   https://docs.djangoproject.com/en/4.0/ref/models/querysets/#values
    
    user = request.user
    qs_my_billing_profile = BillingProfile.objects.filter(user = request.user).values('id')

    print(qs_my_billing_profile[0]['id']) 

    qs_my_orders_by_billing_profile = OrderCheckout.objects.filter(billing_profile = qs_my_billing_profile[0]['id'])
    print(qs_my_orders_by_billing_profile)

    #   trebuie prelucrat raspunsul de la {{order.cart.products.all}} pentru ca da un query set de forma: "<QuerySet [<Product: Earings Swaroski>]>"

    context = {
        'my_orders': qs_my_orders_by_billing_profile
    }
    
    return render(request, "order_history.html", context)

def order_tracking(request):
    return render(request, "order_tracking.html", {})
