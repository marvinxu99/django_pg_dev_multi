from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.apps import apps
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import transaction
import json

from core.constants import ENTRY_MODE, RESULT_STATUS, TRANSACTION_TYPE
from core.models import TransEvent, TransItem


@login_required
@require_POST
@transaction.atomic
def save_trans_data(request):
    '''
    (1) Save transaction event + (2) save the items included in the transaction
    '''
    # # Only accept POST
    # if request.method != 'POST':
    #     return { 'status': 'F' }

    trans_data = json.loads(request.body)
    num_trans_items = len(trans_data['allItems'])

    # Save data
    try:
        # 1. Save transaction event
        trans_event_pk = save_trans_event(trans_data)
        print(trans_event_pk)

        # 2. Save transaction items
        save_trans_items(trans_data, trans_event_pk)

        resp = {
            'status': 'S',         # 'S': successful, 'F': Failed
            'item_count': num_trans_items,
        }
    except Exception as e:
        print(e)
        resp = {
            'status': 'F',         # 'S': successful, 'F': Failed
            'item_count': num_trans_items,
            'error': str(e)
        }

    return JsonResponse(resp)


@transaction.atomic
def save_trans_event(trans_data):
    # Save data
    try:
        te_rec = TransEvent()

        te_rec.authentic_flag = 1
        te_rec.client_id = 12345
        te_rec.coupon_amount = 0
        te_rec.coupon_used_ind = False
        te_rec.entry_mode_cd = ENTRY_MODE.SCAN_N_PAY
        te_rec.event_cd = 0
        te_rec.event_class_cd = 0
        te_rec.event_tag = 'test'
        te_rec.event_title = 'test'
        te_rec.parent_entity_id = 0
        te_rec.parent_entity_name = 'test'
        te_rec.performed_dt_tm = timezone.now()
        te_rec.performed_prsnl_id = trans_data['operator_id']
        te_rec.person_id = 123456
        te_rec.result_status_cd = RESULT_STATUS.AUTH
        te_rec.sequence = 1
        te_rec.total_discount = trans_data['totals']['discount']
        te_rec.total_orig_price = trans_data['totals']['originalPrice']
        te_rec.total_price =  trans_data['totals']['price']
        te_rec.total_quantity =  trans_data['totals']['quantity']
        te_rec.trans_comment_ind = True
        te_rec.trans_end_dt_tm = timezone.now()
        te_rec.trans_start_dt_tm = timezone.now()
        te_rec.trans_type_cd = TRANSACTION_TYPE.PURCHASE
        te_rec.updt_applabel = apps.get_app_config('scan_n_pay').name
        te_rec.updt_cnt = 0
        te_rec.updt_id = 1234
        te_rec.updt_task = 1234
        te_rec.verified_dt_tm = timezone.now()
        te_rec.verified_prsnl_id = trans_data['operator_id']
        te_rec.workstation_id = trans_data['terminal_id']

        te_rec.save()

        if not te_rec.event_id:
            te_rec.event_id = te_rec.trans_event_id
            te_rec.save()
            print('save event_id after created')

    except Exception as e:
        raise e

    return te_rec.trans_event_id


# Save the items to the database
def save_trans_items(trans_data, event_id):

    items = trans_data['allItems']

    try:
        trans_items = []
        for i in range(len(items)):
            trans_items.append(
                TransItem(
                    event_id = event_id,
                    item_id = items[i]['itemId'],
                    item_identifier_id = items[i]['itemIdentId'],
                    item_price_id = items[i]['itemPriceId'],
                    item_discount_id = 0,
                    description = items[i]['description'],
                    quantity = items[i]['quantity'],
                    price =  items[i]['price'],
                    discountAmount = items[i]['price'],
                    price_final = items[i]['priceFinal'],
                    comment = items[i]['comment'],
                    updt_cnt = 0,
                    updt_dt_tm = timezone.now(),
                    updt_id = trans_data['operator_id'],
                    updt_task = 1234,
                    updt_applabel = apps.get_app_config('scan_n_pay').name,
                )
            )
        #print(trans_items)
        TransItem.objects.bulk_create(trans_items)
    except Exception as e:
        raise e
