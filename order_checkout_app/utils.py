import random, string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return 'KRYPNITE_'+''.join(random.choice(chars) for _ in range(size))


def unique_random_order_id(instance):
    """
    This is for a Django project with an order_id field.
    """
    order_new_id = random_string_generator()

    Class = instance.__class__
    qs_exists = Class.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_random_order_id(instance)
    return order_new_id