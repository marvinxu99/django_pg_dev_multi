import datetime
from django.shortcuts import render
from django.conf import settings
import json
import os
import requests
from urllib.request import urlretrieve
from urllib.parse import urlparse
from django.core.files import File
from django.contrib.auth.decorators import permission_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q

from ..models import Product, Order
from core.models import CodeValue


@permission_required('product.can_load_shop_data')
def shop_data_manager(request):
    ''' Shop data manager - default to view today's orders
    '''
    orders_today = Order.objects.filter(create_dt_tm__date=datetime.date.today()).order_by('-create_dt_tm')

    context = {
        'orders': orders_today,
        'page_title': f'Orders, today\'s ({orders_today.count()} orders)',
    }

    return render(request, "shop/data_manager/shop_data_manager.html", context)


@permission_required('product.can_load_shop_data')
def sdm_manage_orders(request):
    ''' Shop data manager - Manage orders
    '''
    data = dict()
    page_title = ''
    orders = []
    
    orders = Order.objects.filter(create_dt_tm__date=datetime.date.today()).order_by('-create_dt_tm')
    page_title = f'Orders, today\'s ({ orders.count() } orders)'
    context = {
        'orders': orders,
        'page_title': page_title
    }

    data['html_sdm_content_pane'] = render_to_string('shop/data_manager/partial_sdm_view_orders.html', context) 
    data['html_sdm_sidebar_nav_1'] = render_to_string('shop/data_manager/partial_sdm_sidenav_orders.html') 
    data['status'] = 'S'

    return JsonResponse(data)


@permission_required('product.can_load_shop_data')
def sdm_manage_orders_filter(request):
    ''' Shop data manager - Manage orders
    '''
    data = dict()
    page_title = ''
    orders = []
    
    timeframe = request.GET['timeframe']

    if timeframe == 'today':
        orders = Order.objects.filter(create_dt_tm__date=datetime.date.today()).order_by('-create_dt_tm')
        page_title = f'Orders, today\'s ({ orders.count() } orders)'
    elif timeframe == 'last2days':
        last2days = datetime.date.today() - datetime.timedelta(days=2)
        orders = Order.objects.filter(Q(create_dt_tm__gte=last2days)).order_by('-create_dt_tm')
        page_title = f'Orders, last 2 days ({ orders.count() } orders)'
    elif timeframe == 'last3days':
        last3days = datetime.date.today() - datetime.timedelta(days=3)
        orders = Order.objects.filter(Q(create_dt_tm__gte=last3days)).order_by('-create_dt_tm')
        page_title = f'Orders, last 3 days ({ orders.count() } orders)'
    elif timeframe == 'last7days':
        last7days = datetime.date.today() - datetime.timedelta(days=7)
        orders = Order.objects.filter(Q(create_dt_tm__gte=last7days)).order_by('-create_dt_tm')
        page_title = f'Orders, last 7 days ({ orders.count() } orders)'

    context = {
        'orders': orders,
        'page_title': page_title
    }

    data['html_sdm_content_pane'] = render_to_string('shop/data_manager/partial_sdm_view_orders.html', context) 
    data['status'] = 'S'

    return JsonResponse(data)


@permission_required('product.can_load_shop_data')
def sdm_manage_products(request):
    ''' Shop data manager - Manage products
    '''
    data = dict()

    page_title = 'Products Page'

    context = {
        'page_title': page_title
    }

    data['html_sdm_content_pane'] = render_to_string('shop/data_manager/partial_sdm_view_products.html', context) 
    data['html_sdm_sidebar_nav_1'] = render_to_string('shop/data_manager/partial_sdm_sidenav_products.html') 
    data['status'] = 'S'

    return JsonResponse(data)
