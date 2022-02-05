from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('products/', views.viewProducts, name='products'),
    # re_path(r'^products/filter/?price=(?P<price>[\w-]+)', views.filterProductsByPrice, name='filter'),
    path('products/filter/', views.filterProductsByPrice, name='filterByPrice'),
    path('products/new-arrivals', views.viewNewArrivalsProducts, name='new-arrivals'),
    re_path(r'^products/(?P<slug>[\w-]+)/',login_required(views.ViewDetailedProduct.as_view()), name='products'),
    path('login/', views.doLogin, name='login'),
    path('register/', views.doRegister, name='register'),
    path('logout/', views.doLogout, name='logout'),
    path('membership/', views.becomeMember, name='membership'),
    path('wishlist/', views.getWishlist, name='wishlist'),
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)