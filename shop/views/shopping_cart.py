from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum

from shop.models import Cart, CartItem


# @login_required(login_url='/accounts/login/')
@require_POST
def add_to_cart(request, pk):
    """ Add product to Cart
    """
    data = dict()
    data["item_count"] = 0

    if request.user == AnonymousUser():
        print(request.user)
        data['status'] = 'F'
    else:
        cart, created = Cart.objects.get_or_create(owner=request.user) 
        if created:
            cart.description = "SHOPPING_CART"
            cart.create_id = request.user.user_id
            cart.save()
        print(cart) 

        cart_item, created = CartItem.objects.get_or_create(cart_id=cart.cart_id, item_id=pk)
        if created:
            cart_item.create_id = request.user.user_id
            cart_item.save()            
        else:
            cart_item.quantity += 1
            cart_item.updt_id = request.user.user_id
            cart_item.save()

        d_result = CartItem.objects.filter(cart_id=cart.cart_id).aggregate(Sum('quantity'))

        data['item_count'] = d_result['quantity__sum']  
        data['status'] = 'S'

    return JsonResponse(data)



