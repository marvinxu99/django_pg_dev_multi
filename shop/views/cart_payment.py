from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse


from shop.models import Cart, CartItem, Product, Payment, Order, OrderItem
from core.models import CodeValue


@login_required
def cart_pay_success(request):
    '''Logics after a successful payment was made
    '''
    items = []
    order = None

    cart = get_object_or_404(Cart, owner=request.user) 
    cart_items = CartItem.objects.filter(cart=cart)
    d_result = CartItem.objects.filter(cart_id=cart.cart_id).aggregate(Sum('quantity'), Sum('price'))

    # This is also to prevent resubmit when user refreshes the payment sucessful page
    if (not d_result['quantity__sum']) or (not d_result['price__sum']):
        return HttpResponseRedirect(reverse("shop:shop_home"))

    #with transaction.Atomic():
     
    # Create a payment record
    payment = Payment.objects.create(
        description = "Credit payment", 
        amount = d_result['price__sum'] if d_result['price__sum'] else 0,
        comment = "stripe payment"
    )

    # Create an order
    order = Order(owner=request.user)
    order.description = "Online purchase"
    order.quantity = d_result['quantity__sum'] if d_result['quantity__sum'] else 0
    order.total = d_result['price__sum'] if d_result['price__sum'] else 0
    order.payment = payment
    order.comment = "paid by stripe"
    order.save()

    # Populate order items to OrderItem table (?? using map())
    for item in cart_items:
        OrderItem.objects.create(
            order_id = order.order_id,
            product_id = item.product.id,
            quantity = item.quantity,
            price = item.price
        )

    # Remove all items from the cart
    CartItem.objects.filter(cart=cart).delete()


    # codeset 2 is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    items = OrderItem.objects.filter(order=order)
    o_result = OrderItem.objects.filter(order=order).aggregate(Sum('price'))
    
    context = {
        'items': items,
        'categories': categories,
        'page_title': "Payment Successful",
        'order_total': o_result['price__sum'] if o_result['price__sum'] else 0,
    }

    return render(request, "shop/cart_pay_success.html", context)


@login_required
def cart_pay_cancelled(request):
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
