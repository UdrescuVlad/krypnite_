from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('add-product/', views.addProduct, name='addProduct'),
    path('change-order-status/', views.changeOrderStatus, name='changeOrderStatus'),
    path('view-users', views.viewUsers, name='viewUsers')
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)