from django.shortcuts import render
import stripe
# Create your views here.

STRIPE_PUB_KEY = "pk_test_51KQFEFHR2u8dAKpeNYZ93U3Anb5yImjZMLmvoEWODzyVXaQI7lQ7KGtcIlRczjeizgSjvoodyyFeYL26e3xk3pNL00LwGwatBh"
stripe.api_key = "sk_test_51KQFEFHR2u8dAKpeMxn4TbjNfMuWKo93gq4ojSVkVAzGd1B09aH8OqgNrWGqSw17lQ7jjn3CEqjoqoMkWQET1mOC00MEaPzEGv"

#   publish key will go to FE
#   https://stripe.com/docs/payments/elements

def do_pay(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'payment_view2.html',{"pub_key":STRIPE_PUB_KEY})