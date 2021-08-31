from django.shortcuts import render
from krypniteweb.templates import *

# Create your views here.

def viewProducts(request):
    return render(request, 'view_products.html')