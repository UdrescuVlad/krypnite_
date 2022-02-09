from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from admin_dash_app.forms import OrderCheckoutForm, ProductForm
from order_checkout_app.models import OrderCheckout
from django.db.models import Q

#   https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.decorators.user_passes_test
#   https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.User.has_perm
#   https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.User.is_superuser


def verify_user_is_superuser(user):
    return user.is_superuser

def verify_user_has_perms_add_product(user):
    return user.has_perm('product.can_add_product')


# @user_passes_test(verify_user_has_perms_add_product)
@user_passes_test(verify_user_is_superuser)
def addProduct(request):
    #   https://forum.djangoproject.com/t/image-does-not-save/4664
    add_product_form = ProductForm(request.POST, request.FILES or None)
    if add_product_form.is_valid():
        add_product_form.save()
        add_product_form = ProductForm()

    context = {
        'add_product_form': add_product_form
    }
    return render(request, 'add_product.html', context)

@user_passes_test(verify_user_is_superuser)
def changeOrderStatus(request):
    #   am nevoie de 2 field-uri: un input unde user-ul va introduce ext_id si un dropdown de status

    get_all_ext_id = OrderCheckout.objects.all()
    change_status_form = OrderCheckoutForm(request.POST or None)

    if change_status_form.is_valid():
        order_ext_id = change_status_form.cleaned_data.get("order_ext_id")
        status = change_status_form.cleaned_data.get("status")
        query_set = OrderCheckout.objects.filter(Q(order_ext_id__exact=order_ext_id))
        if query_set is not None:
            OrderCheckout.objects.filter(order_ext_id=order_ext_id).update(status=status)
            change_status_form = OrderCheckoutForm()
            
    context = {
        "get_all_ext_id": get_all_ext_id,
        "change_status_form": change_status_form
    }
    return render(request, 'change_order_status.html', context)

@user_passes_test(verify_user_is_superuser)
def viewUsers(request):

    context = {
    }
    return render(request, 'view_users.html', context)