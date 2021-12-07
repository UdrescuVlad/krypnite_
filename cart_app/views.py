from django.shortcuts import render
from .models import Cart

def cart_home(request):

    cart_id = request.session.get("cart_id", None)
    print(cart_id)
    query = Cart.objects.filter(id=cart_id)
    if query.count() == 1:
        cart_object = query.first()
        if request.user.is_authenticated and cart_object.user is None:
            cart_object.user = request.user
            cart_object.save()
    else:
        cart_object = Cart.objects.new(user=request.user)
        request.session['cart_id'] = cart_object.id
    
    return render(request, "home.html", {})