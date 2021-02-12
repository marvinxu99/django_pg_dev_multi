import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from core.models import ItemBarcode, ItemIdentifier, ItemPrice
from core.constants import ITEM_BARCODE_TYPE, ITEM_IDENTIFIER_TYPE, ITEM_PRICE_TYPE


# Home of scan_n_pay app
@login_required
def scan_n_pay(request):
    # # print("app: " + apps.get_app_config('scan_n_pay').name)
    # for app in apps.get_app_configs():
    #     #print(app.name, app.verbose_name, app.label, app.path)
    #     print(app.label)

    query = request.GET.get('q')
    if query:
        print("q= " + query)

    # if query:
    #     author_list = self.model.objects.filter(
    #         Q(first_name__icontains=query) | Q(last_name__icontains=query)
    #     )
    # else:
    #     author_list = self.model.objects.all()
    # #return Author.objects.filter(name__icontains='war')[:5] # Get 5 books containing the title war
    # return author_list

    return render(request, 'scan_n_pay/scan_n_pay.html')

# Return the item information as per Barcode
# for urls like "/scan/?barcode=12345"
@login_required
def get_item(request):

    barcode = request.GET.get('barcode')
    if barcode:
        print('barcode: ' + barcode)

    # Default return data if not found.
    data = {
        'validInd': 1,
        'itemId': -1,
        'itemIdentId': -1,
        'itemPriceId': -1,
        'description': 'NOT FOUND',
        'price': -0.01,
    }

    try:
        # Query the item_id from ITEM_BARCODE table
        item_id = ItemBarcode.objects.filter(
                    active_ind = True,
                    item_barcode_type_cd = ITEM_BARCODE_TYPE.BARCODE,
                    value = barcode
                )[0].item.pk
        data['itemId'] = item_id

        # Query the item description from the ITEM_IDENTIFIER table
        item_ident = ItemIdentifier.objects.filter(
                    active_ind = True,
                    item_identifier_type_cd = ITEM_IDENTIFIER_TYPE.DESCRIPTION,
                    item_id = item_id
                    )[0]
        data['description'] = item_ident.value
        data['itemIdentId'] = item_ident.item_identifier_id

        # Query the item price from the ITEM_PRICE table
        item_price = ItemPrice.objects.filter(
                    active_ind = True,
                    price_type_cd = ITEM_PRICE_TYPE.QUOTE,
                    item_id = item_id
                    )[0]
        data['price'] = item_price.price_float()
        data['itemPriceId'] = item_price.item_price_id

    except Exception:
        if data['itemId'] == -1:
            print("query database error: product not found.")
        if data['price'] == -0.01:
            print('query database error: price not found')
        data['validInd'] = 0


    return JsonResponse(data)


def pay_successful(request):
    return render(request, 'scan_n_pay/pay_successful.html')
