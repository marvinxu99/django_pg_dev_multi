import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, reverse


@login_required
# @require_POST
def add_to_cart(request, pk):
    """ Add product to Cart
    """
    data = dict()
    data['status'] = 'S'

    return JsonResponse(data)
