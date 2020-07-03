import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from core.models import Item, ItemBarcode, ItemIdentifier, ItemPrice
from core.constants import ITEM_BARCODE_TYPE, ITEM_IDENTIFIER_TYPE, ITEM_PRICE_TYPE
from core.constants import ITEM_TYPE


def search_products(request):
    # item types to search for
    search_item_types = [
        ITEM_TYPE.GENERAL,
        ITEM_TYPE.PRODUCE,
        ITEM_TYPE.DAIRY,
    ]
        
    # Item
    qs_items = Item.objects.filter(active_ind=True, item_type_cd__in=search_item_types)
    print(qs_items)
    items_count = len(qs_items)
    print(f'item_count = {items_count}')

    # ItemIdentifier
    qs_identifier = qs_items[0].Identifiers.filter(
            active_ind = True,
            item_identifier_type_cd = ITEM_IDENTIFIER_TYPE.DESCRIPTION
        )[0]
    item_identifier_id = qs_identifier.item_identifier_id 
    print(f'item identifier id = {item_identifier_id}')

    # ItemPrice
    qs_price = qs_items[0].Prices.filter(price_type_cd = ITEM_PRICE_TYPE.QUOTE)[0]
    item_price_id = qs_price.item_price_id
    price = qs_price.price
    print(f'item_price_id = {item_price_id }, price = {price}')


    data = {
        'itemsCount': 0,
        'items': [
            {
                'itemId': -1,
                'itemIdentId': -1,
                'itemPriceId': -1,
                'description': '',
                'price': -0.01,
            },
        ],
    }

    return JsonResponse(data)
