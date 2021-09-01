from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from krypniteweb.templates import *

# Create your views here.

def viewProducts(request):
    return render(request, 'view_products.html')

def doLogout(request):
    logout (request)
    return render(request, 'login.html')

def doLogin(request):
    if request.user.is_authenticated:
        return redirect('products')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                context = messages.success(request, username+', welcome')
                return redirect('/krypnite/products')
            else:
                context = messages.error(request, 'Username or password is incorrect.')
                return render(request, 'login.html', context)
        return render(request, 'login.html')

def doRegister(request):
    return render(request, 'register.html')