from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db import transaction


from shop.models import Product, Payment, Order, OrderItem
from core.models import CodeValue


@login_required
def view_orders(request):
    '''Logics after a successful payment was made
    '''
    items = []

    # codeset 2 is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    # Create an order
    orders = Order.objects.filter(owner=request.user).order_by('-create_dt_tm')

    items = OrderItem.objects.filter(order=orders[0])
    o_result = OrderItem.objects.filter(order=orders[0]).aggregate(Sum('price'))
    
    context = {
        'orders': orders,
        'items': items,
        'page_title': "Your orders",
        'order_total': o_result['price__sum'] if o_result['price__sum'] else 0,
        'categories': categories,
        'filter_name': 'My Last Order'
    }

    return render(request, "shop/shop_orders.html", context)

@login_required
def view_orders_filter(request):
    '''Logics after a successful payment was made
    '''
    items = []

    # codeset 2 is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    # Create an order
    orders = Order.objects.filter(owner=request.user).order_by('-create_dt_tm')

    items = OrderItem.objects.filter(order=orders[0])
    o_result = OrderItem.objects.filter(order=orders[0]).aggregate(Sum('price'))
    
    context = {
        'orders': orders,
        'items': items,
        'page_title': "Your orders",
        'order_total': o_result['price__sum'] if o_result['price__sum'] else 0,
        'categories': categories,
        'filter_name': 'My Last Order'
    }

    return render(request, "shop/shop_orders.html", context)

