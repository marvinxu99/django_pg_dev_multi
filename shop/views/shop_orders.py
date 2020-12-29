from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from shop.models import Product, Payment, Order, OrderItem
from core.models import CodeValue


@login_required
def view_orders(request):
    '''Logics after a successful payment was made
    '''
    # codeset 2 is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    # Get the last order
    order = Order.objects.filter(owner=request.user).order_by('-create_dt_tm').first()
    orders = [order] if order else None

    context = {
        'orders': orders,
        'page_title': _("Your orders"),
        'categories': categories,
        'filter_name': _('My Last Order')
    }

    return render(request, "shop/shop_orders.html", context)


@login_required
def view_orders_filter(request):

    data = dict()
    filter_name = ''

    filter = request.GET['filter']
    
    orders_all = Order.objects.filter(owner=request.user).order_by('-create_dt_tm')

    if filter == 'my-last-order':
        orders = [ orders_all[0] ] if orders_all else None
        filter_name = _('My Last Order')
    elif filter == 'my-last-3-orders':
        orders = orders_all[:3]
        filter_name = _('My Last 3 Orders')
    else:
        orders = orders_all
        filter_name = _('All My Orders')

    data['html_view_orders'] = render_to_string(
                'includes/partial_view_orders.html', 
                { 'orders': orders }
            )
    data['filter_name'] = filter_name

    return JsonResponse(data)


@login_required
def view_orders_orderid(request, orderid):
    data = dict()
    filter_name = ''

    order = Order.objects.get(order_id=orderid)

    orders = [order, ]
    filter_name = _("Order placed on") + " " + order.create_dt_tm.strftime("%d-%b-%Y")

    data['html_view_orders'] = render_to_string(
                'includes/partial_view_orders.html', 
                { 'orders': orders }
            )
    data['filter_name'] = filter_name

    return JsonResponse(data)
