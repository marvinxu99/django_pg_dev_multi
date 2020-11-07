from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum
from django.shortcuts import render
from django.shortcuts import get_object_or_404


from shop.models import Cart, CartItem
from core.models import CodeValue


# @login_required(login_url='/accounts/login/')
@require_POST
def cart_add_item(request, pk):
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


@login_required
def cart_item_count(request):
    """ Add product to Cart
    """
    data = dict()

    if request.user == AnonymousUser():
        print(request.user)
        data['status'] = 'F'
    else:
        cart, created = Cart.objects.get_or_create(owner=request.user) 
        if created:
            cart.description = "SHOPPING_CART"
            cart.create_id = request.user.user_id
            cart.save()

        d_result = CartItem.objects.filter(cart_id=cart.cart_id).aggregate(Sum('quantity'))

        if d_result['quantity__sum']:
            data['item_count'] = d_result['quantity__sum']
        else:  
            data["item_count"] = 0

        data['status'] = 'S'

    return JsonResponse(data)


@login_required
def cart_view_items(request):

    # codeset 2(2) is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    cart = get_object_or_404(Cart, owner=request.user) 
    items = CartItem.objects.filter(cart=cart)
   

    context = {
        'items': items,
        'categories': categories,
        'page_title': "Shopping Cart"
    }

    return render(request, "shop/shop_cart.html", context)
