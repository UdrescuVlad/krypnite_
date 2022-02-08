from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.searchViewByProduct, name='byProductName'),
    path('category/', views.searchByCategoryProduct, name='byCategory'),
    path('extID/', views.searchOrderExtId, name='byExtID'),
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)