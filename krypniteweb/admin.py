from django.contrib import admin

from krypniteweb.models import Product,Wishlist

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'location', 'category', 'in_stock', 'new_arrivals', 'slug']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(Wishlist)