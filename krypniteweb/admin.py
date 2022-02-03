from django.contrib import admin

from krypniteweb.models import Product,Wishlist

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'location']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(Wishlist)