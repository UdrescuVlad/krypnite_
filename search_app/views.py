from errno import EILSEQ
from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart_app.models import Cart
from krypniteweb.models import Product
from django.db.models import Q

from order_checkout_app.models import OrderCheckout

@login_required
def searchViewByProduct(request):
    get_q = request.GET.get('q', None)  # al 2-lea parametru este pentru valoarea default
    if get_q is not None:
        multiple_search = Q(product_name__icontains=get_q) | Q(description__icontains=get_q) | Q(category__icontains=get_q)
        query_set = Product.objects.filter(multiple_search).distinct()  # folosim distinct ca in cazul in care multiple_search returneaza acelasi produs de 2 ori sa il ia doar o data
    else:
        query_set = Product.objects.all()
    
    context={
        'products':query_set 
    }

    return render(request, 'view_products_on_search.html', context)

@login_required
def searchByCategoryProduct(request):
    get_q = request.GET.get('q', None)  # al 2-lea parametru este pentru valoarea default
    if get_q is not None:
        query_set = Product.objects.filter(Q(category__icontains=get_q))  # folosim distinct ca in cazul in care multiple_search returneaza acelasi produs de 2 ori sa il ia doar o data
    else:
        query_set = Product.objects.all()

    context={
        'products':query_set 
    }
    return render(request, 'view_products_on_search_by_category.html', context)

def searchOrderExtId(request):
    get_q = request.GET.get('q', None)
    if get_q is not None:
        query_ext_id = OrderCheckout.objects.filter(Q(order_ext_id__exact=get_q))
    else:
        query_ext_id = None
    print(query_ext_id)

    context = {
        'searchead_ext_id':query_ext_id
    }
    return render(request, 'order_tracking.html', context)