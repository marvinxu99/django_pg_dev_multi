from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json


@csrf_exempt
def save_trans_data(request):
    # accept POST
    if request.method != 'POST':
        return { 'status': 'F' }

    transdata = json.loads(request.body) 
    print(transdata)
    print(f"there are { len(transdata['allItems']) } items in the transdata.")
    
    # Save data to databse




    resp_s = {
        'status': 'S',         # 'S': successful, 'F': Failed 
        'item_count': len(transdata['allItems']),
    }
    return JsonResponse(resp_s)
