from django.contrib import admin

from billing_app.models import BillingProfile

class BillingProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__','user']
    class Meta:
        model = BillingProfile


admin.site.register(BillingProfile, BillingProfileAdmin)