import os
import requests
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http.response import JsonResponse
from django.template.loader import render_to_string
import json

@login_required()
@require_POST
def core_code_builder(request):
    pass
