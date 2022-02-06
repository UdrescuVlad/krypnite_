from django.db import models
from django.conf import settings
from django.db.models.signals import post_save,pre_save
import stripe

# class BillingProfileManager(models.Manager):
#     def new_or_get(self, request):
#         if request.user.is_authenticated():
#             obj

#   Test mode
stripe.api_key = "sk_test_51KQFEFHR2u8dAKpeMxn4TbjNfMuWKo93gq4ojSVkVAzGd1B09aH8OqgNrWGqSw17lQ7jjn3CEqjoqoMkWQET1mOC00MEaPzEGv"


User = settings.AUTH_USER_MODEL

#   admin@admin.ro -> poate sa aiba 1k de billing profile
#   dar, user-ul admin@admin.ro -> ar trebui sa aiba doar un billing profile
class BillingProfile(models.Model):
    #   la user putem folosim ForeignKey cu unique=True <=> cu folosirea OneToOneField
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    customer_payment_id = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.email


#   https://stripe.com/docs/invoicing/customer?dashboard-or-api=api
def pre_save_billing_profile(sender, instance, *args, **kwargs):
    if not instance.customer_payment_id and instance.email:
        print("assign ext id from stripe to this user")
        customer_stripe = stripe.Customer.create(email=instance.email)
        instance.customer_payment_id = customer_stripe.id
        print(customer_stripe)
        
pre_save.connect(pre_save_billing_profile, sender=BillingProfile)

def post_save_user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)
#   oricand cand un user este creat ii este creat automat si un billing profile
post_save.connect(post_save_user_created_receiver, sender=User)
