import random, string

def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return 'KRYPNITE_'+''.join(random.choice(chars) for _ in range(size))

def unique_random_order_id(instance):
    
    order_new_id = random_string_generator()

    Class = instance.__class__
    qs_exists = Class.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_random_order_id(instance)
    return order_new_id


def random_ext_id_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return 'KRYPNITE_DELIVERY_'+''.join(random.choice(chars) for _ in range(size))

def unique_random_order_ext_id(instance):

    order_new_ext_id = random_ext_id_string_generator()
    qs_exists = instance.objects.filter(order_id=order_new_ext_id).exists()
    if qs_exists:
        return unique_random_order_ext_id(instance)
    return order_new_ext_id