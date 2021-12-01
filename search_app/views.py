from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from krypniteweb.models import Product

@login_required
def searchViewByProduct(request):
    print(request.GET)
    get_q = request.GET.get('q', None)  # al 2-lea parametru este pentru valoarea default
    print(get_q)
    if get_q is not None:
        query_set = Product.objects.filter(product_name__icontains=get_q)
    else:
        query_set = Product.objects.all()
    
    context={
        'products':query_set
    }
    return render(request, 'view_products_on_search.html', context)