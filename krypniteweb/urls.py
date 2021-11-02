from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('products/', views.viewProducts, name='products'),
    path('login/', views.doLogin, name='login'),
    path('logout/', views.doLogout, name='logout'),
    path('register/', views.doRegister, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 