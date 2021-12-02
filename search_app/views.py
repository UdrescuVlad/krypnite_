from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from krypniteweb.models import Product
from django.db.models import Q

@login_required
def searchViewByProduct(request):
    print(request.GET)
    get_q = request.GET.get('q', None)  # al 2-lea parametru este pentru valoarea default
    print(get_q)
    if get_q is not None:
        multiple_search = Q(product_name__icontains=get_q) | Q(description__icontains=get_q)
        query_set = Product.objects.filter(multiple_search).distinct()  # folosim distinct ca in cazul in care multiple_search returneaza acelasi produs de 2 ori sa il ia doar o data
    else:
        query_set = Product.objects.all()
    
    context={
        'products':query_set
    }
    return render(request, 'view_products_on_search.html', context)