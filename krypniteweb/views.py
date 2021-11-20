from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from krypniteweb.models import Product
from krypniteweb.forms import WishlistForm, RegistrationModelForm
from krypniteweb.templates import *
from django.contrib.auth.decorators import login_required

@login_required
def viewProducts(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products':products})

@login_required
def becomeMember(request):
    return render(request, 'become_member.html')

@login_required
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
        return redirect('/krypnite/products/')
    else:
        if request.method == 'POST':
            username1 = request.POST.get('username')
            password1 = request.POST.get('password')
            user = authenticate(request, username=username1, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, username1+', welcome')
                return redirect('/krypnite/products/')
            else:
                messages.error(request, 'Username or password is incorrect.')
                return render(request, 'login.html')
        return render(request, 'login.html')

User = get_user_model()
def doRegister(request):
    context = {}
    form = RegistrationModelForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        User.objects.create_user()
    context['registration_form'] = form
    return render(request, 'register.html', context)