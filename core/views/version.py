from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
def version_info(request):
    pass
