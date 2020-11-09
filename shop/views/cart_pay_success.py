from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404


from shop.models import Cart, CartItem, Product
from core.models import CodeValue


@login_required
def cart_pay_success(request):
    '''Logics after a successful payment was made
    '''
    cart = get_object_or_404(Cart, owner=request.user) 
    items = CartItem.objects.filter(cart=cart)

    # Concert cart items to an order - order info to be stored in Order, OrderItem
    items = CartItem.objects.filter(cart=cart)

    # Remove all items from the cart
    items = CartItem.objects.filter(cart=cart)
    CartItem.objects.filter(cart=cart).delete()

    # codeset 2(2) is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    context = {
        'items': None,
        'categories': categories,
        'page_title': "Successfull Payment",
        'cart_total': 0,
    }

    return render(request, "shop/stripe/pay_successful.html", context)

