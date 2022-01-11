from django.db.models import query
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DetailView
from krypniteweb.models import Product
from cart_app.models import Cart
from krypniteweb.forms import WishlistForm, RegistrationModelForm
from krypniteweb.templates import *

from django.contrib.auth.decorators import login_required

@login_required
def viewProducts(request):
    query_set = Product.objects.all()
    cart_obj, new_or_not = Cart.objects.new_or_get(request)
    context={
        'products':query_set,
        'cart':cart_obj
    }
    return render(request, 'view_products.html', context)

class ViewDetailedProduct(DetailView):
    query_set = Product.objects.all()
    template_name = 'view_detail_product.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ViewDetailedProduct, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug)
            
        except Product.DoesNotExist:
            raise Http404("There is nothing to see here...")
        except Product.MultipleObjectsReturned:
            query_set = Product.objects.filter(slug=slug)
            instance = query_set.first
        except:
            raise Http404("Fall back to safe zone!")
        return instance


# def viewDetailedProduct(request, id):
#     instance = get_object_or_404(Product, id=int(id))
#     context={
#         'object':instance
#     }
#     return render(request, 'view_detail_product.html', context)

# def viewDetailedProductBySlug(request, slug):
#     try:
#         instance = Product.objects.get(slug=slug)
#     except Product.DoesNotExist:
#         raise Http404("There is nothing to see here...")
#     except Product.MultipleObjectsReturned:
#         query_set = Product.objects.filter(slug=slug)
#         instance = query_set.first
#     except:
#         raise Http404("Fall back to safe zone!")
#     context={
#         'product':instance
#     }
#     return render(request, 'view_detail_product.html', context)

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
    form = RegistrationModelForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(name, email, password)
        form = RegistrationModelForm()
        print(new_user)

    context['registration_form'] = form
    return render(request, 'register.html', context)
