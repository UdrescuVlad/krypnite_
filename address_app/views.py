from django.shortcuts import render, redirect

from address_app.forms import AddressForm
from billing_app.models import BillingProfile

def billing_info_redirect(request): 
    billing_address_form = AddressForm(request.POST or None)
    context = {
        'billing_address_form':billing_address_form
    }
    if billing_address_form.is_valid():
        print(request.POST)
        instance = billing_address_form.save()
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(request)
        if billing_profile is not None:
            instance.billing_profile = billing_profile
            instance.save()
        else:
            print("Please reauthenticate!")
            return  redirect("krypnite:logout")
    return render(request, 'address_billing.html', context)
    # return redirect('address:billing')