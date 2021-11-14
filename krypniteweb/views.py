from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from krypniteweb.models import Product
from krypniteweb.forms import WishlistForm
from krypniteweb.templates import *

# Create your views here.

def viewProducts(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products':products})

def becomeMember(request):
    return render(request, 'become_member.html')

def getWishlist(request):
    context = {}
    form = WishlistForm(request.POST)
    if form.is_valid():
        form.save()
        form = WishlistForm()
    context['wishlist_form'] = form
    return render(request, 'get_wishlist.html', context)

def doLogout(request):
    logout (request)
    return redirect('/krypnite/login')

def doLogin(request):
    if request.user.is_authenticated:
        return redirect('/krypnite/products')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                context = messages.success(request, username+', welcome')
                return redirect('/krypnite/products', context)
            else:
                context = messages.error(request, 'Username or password is incorrect.')
                return render(request, 'login.html', context)
        return render(request, 'login.html')

def doRegister(request):
    return render(request, 'register.html')