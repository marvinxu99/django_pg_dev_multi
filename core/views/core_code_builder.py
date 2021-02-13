import json
import os

import requests
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET, require_POST


@login_required()
@require_POST
def core_code_builder(request):
    pass
