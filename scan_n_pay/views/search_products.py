import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from core.models import ItemBarcode, ItemIdentifier, ItemPrice
from core.constants import ITEM_BARCODE_TYPE, ITEM_IDENTIFIER_TYPE, ITEM_PRICE_TYPE


def search_products(request):
    # Default return data if not found.
    data = {
        'validInd': 1,
        'itemId': -1,
        'itemIdentId': -1,
        'itemPriceId': -1,
        'description': 'all items',
        'price': -0.01,
    }

    return JsonResponse(data)
