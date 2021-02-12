from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum, Q
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _

from shop.models import Cart, CartItem, Product
from core.models import CodeValue


@login_required(login_url='/accounts/login/')
@require_POST
def cart_add_item(request, pk):
    """ Add a product item to Cart
    """
    data = dict()
    data["cart_count"] = 0
    data["cart_total"] = 0
    data["item_count"] = 0
    data["item_price"] = 0

    if request.user == AnonymousUser():
        print(request.user)
        data['status'] = 'F'
    else:
        cart, created = Cart.objects.get_or_create(owner=request.user)
        if created:
            cart.description = "SHOPPING_CART"
            cart.create_id = request.user.user_id
            cart.save()

        # product = get_object_or_404(Product, pk=pk)
        cart_item, created = CartItem.objects.get_or_create(cart_id=cart.cart_id, product_id=pk)
        if created:
            cart_item.create_id = request.user.user_id
            cart_item.price = cart_item.product.price
            cart_item.save()
        else:
            cart_item.quantity += 1
            cart_item.price = cart_item.product.price * cart_item.quantity
            cart_item.updt_id = request.user.user_id
            cart_item.save()

        d_result = CartItem.objects.filter(cart_id=cart.cart_id).aggregate(Sum('quantity'), Sum('price'))

        data['cart_count'] = d_result['quantity__sum']
        data['cart_total'] = d_result['price__sum'] if d_result['price__sum'] else 0
        data["item_count"] = cart_item.quantity
        data["item_price"] = cart_item.price
        data['status'] = 'S'

    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
@require_POST
def cart_deduct_item(request, pk):
    """ Deduct a product item from Cart
    """
    data = dict()
    data["cart_count"] = 0
    data["cart_total"] = 0
    data["item_count"] = 0
    data["item_price"] = 0

    if request.user == AnonymousUser():
        print(request.user)
        data['status'] = 'F'
    else:
        cart = get_object_or_404(Cart, owner=request.user)

        cart_item = get_object_or_404(CartItem, Q(cart_id=cart.cart_id) & Q(product_id=pk))
        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity = cart_item.quantity - 1
                cart_item.price = cart_item.product.price * cart_item.quantity
                cart_item.updt_id = request.user.user_id
                cart_item.save()
                data['item_count'] = cart_item.quantity
                data['item_price'] = cart_item.price
            else:
                cart_item.delete()

        d_result = CartItem.objects.filter(cart_id=cart.cart_id).aggregate(Sum('quantity'), Sum('price'))

        data['cart_count'] = d_result['quantity__sum']
        data['cart_total'] = d_result['price__sum'] if d_result['price__sum'] else 0
        data['status'] = 'S'

    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
@require_POST
def cart_remove_item(request, pk):
    """ Remove a product (all items for this product) from the cart
    """
    data = dict()
    data["cart_count"] = 0
    data["cart_total"] = 0
    data["item_count"] = 0
    data["item_price"] = 0

    if request.user == AnonymousUser():
        print(request.user)
        data['status'] = 'F'
    else:
        cart = get_object_or_404(Cart, owner=request.user)

        cart_item = get_object_or_404(CartItem, Q(cart_id=cart.cart_id) & Q(product_id=pk))
        if cart_item:
            cart_item.delete()

        d_result = CartItem.objects.filter(cart_id=cart.cart_id).aggregate(Sum('quantity'), Sum('price'))

        data['cart_count'] = d_result['quantity__sum']
        data['cart_total'] = d_result['price__sum'] if d_result['price__sum'] else 0
        data['status'] = 'S'

    return JsonResponse(data)


@login_required
def cart_item_count(request):
    """ Return how many items are there in the cart.
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

    d_result = CartItem.objects.filter(cart_id=cart.cart_id).aggregate(Sum('price'))
    cart_total = d_result['price__sum'] if d_result['price__sum'] else 0

    context = {
        'items': items,
        'categories': categories,
        'page_title': _("Shopping Cart"),
        'cart_total': cart_total,
    }

    return render(request, "shop/shop_cart.html", context)


@login_required
def cart_remove_all_items(request):

    # codeset 2(2) is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    cart = get_object_or_404(Cart, owner=request.user)
    CartItem.objects.filter(cart=cart).delete()

    context = {
        'items': None,
        'categories': categories,
        'page_title': _("Shopping Cart"),
        'cart_total': 0,
    }

    return render(request, "shop/shop_cart.html", context)
