from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('home', views.cart_home, name='home'),
    path('update', views.cart_update, name='update'),
    path('checkout', views.checkout_redirect, name='checkout'),
    path('favhome', views.fav_list_home, name='favhome'),
    path('favupdate', views.fav_list_update, name='favupdate'),
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)