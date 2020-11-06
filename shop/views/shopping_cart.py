from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from shop.models import Cart, CartItem


@login_required()
# @require_POST
def add_to_cart(request, pk):
    """ Add product to Cart
    """
    data = dict()

    cart, created = Cart.objects.get_or_create(owner=request.user) 
    if created:
        cart.description = "SHOPPING_CART"
        cart.save()
    print(cart)


    data['status'] = 'S'

    return JsonResponse(data)



