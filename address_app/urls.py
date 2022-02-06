from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    # path('billing/shipping/', views.billing_shipping_info, name='billing-shipping'),
    path('billing/shipping/validation', views.validation_billing_shipping_info, name='billing-shipping-validation'),
    path('billing/shipping/reuse', views.validation_billing_shipping_info_reuse, name='billing-shipping-reuse'),

] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)