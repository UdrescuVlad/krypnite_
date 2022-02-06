from django.shortcuts import render, redirect

from address_app.forms import AddressForm
from billing_app.models import BillingProfile

def validation_billing_shipping_info(request):
    form = AddressForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(request.POST)
        form_instance = form.save(commit=False)
        billing_profile = None
        if request.user.is_authenticated:
            billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=request.user,email=request.user.email)
        else:
            redirect("krypnite:login")
        if billing_profile is not None:
            address_type = request.POST.get('address_type', 'shipping')
            form_instance.billing_profile = billing_profile
            form_instance.address_type = address_type
            print(form_instance.billing_profile)
            print(form_instance.address_type)
            form_instance.save()

            request.session[address_type + "_address_id"] = form_instance.id
        else:
            print("Billing information is not registered. Please create an account if you don't have one.")
            redirect("krypnite:login")

    return redirect("cart:checkout")