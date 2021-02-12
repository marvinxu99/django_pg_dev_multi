import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


from core.models import Item, ItemBarcode, ItemIdentifier, ItemPrice
from core.constants import ITEM_BARCODE_TYPE, ITEM_IDENTIFIER_TYPE, ITEM_PRICE_TYPE
from core.constants import ITEM_TYPE


@login_required
def search_products(request):

    data = {
        'itemsCount': 0,
        'items': [
            # {
            #     'itemId': -1,
            #     'itemIdentId': -1,
            #     'itemPriceId': -1,
            #     'description': '',
            #     'price': -0.01,
            # },
        ],
    }

    # Item types to search for
    search_item_types = [
        ITEM_TYPE.GENERAL,
        ITEM_TYPE.PRODUCE,
        ITEM_TYPE.DAIRY,
    ]

    # Item
    qs_items = Item.objects.filter(active_ind=True, item_type_cd__in=search_item_types)
    data['itemsCount'] = len(qs_items)
    print(f"item_count = {data['itemsCount']}")

    # # ItemIdentifier
    # qs_identifier = qs_items[0].Identifiers.filter(
    #         active_ind = True,
    #         item_identifier_type_cd = ITEM_IDENTIFIER_TYPE.DESCRIPTION
    #     )[0]
    # item_identifier_id = qs_identifier.item_identifier_id
    # print(f'item identifier id = {item_identifier_id}')

    # # ItemPrice
    # qs_price = qs_items[0].Prices.filter(price_type_cd = ITEM_PRICE_TYPE.QUOTE)[0]
    # item_price_id = qs_price.item_price_id
    # price = qs_price.price
    # print(f'item_price_id = {item_price_id }, price = {price}')

    for item in qs_items:
        item_details = {}
        item_details['itemId'] = item.item_id

        # ItemIdentifier
        qs_identifier = item.Identifiers.filter(
                active_ind = True,
                item_identifier_type_cd = ITEM_IDENTIFIER_TYPE.DESCRIPTION
            )[0]
        item_details['itemIdentId'] = qs_identifier.item_identifier_id
        item_details['description'] = qs_identifier.value
        print(f"item identifier id = {item_details['itemIdentId']}")

        # ItemPrice
        qs_price = item.Prices.filter(price_type_cd = ITEM_PRICE_TYPE.QUOTE)[0]
        item_details['itemPriceId'] = qs_price.item_price_id
        item_details['price'] = qs_price.price
        print(f"item_price_id = {item_details['itemPriceId'] }, price = {item_details['price']}")

        data['items'].append(item_details)

    print(data)

    return JsonResponse(data)
