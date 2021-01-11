from django.shortcuts import render
from django.conf import settings


def domain_info(request):
    context = {
        "DOMAIN": settings.DOMAIN,
        "PROD_DEPLOY": settings.PROD_DEPLOY,
        "DEBUG": settings.DEBUG,
        "ADMINS": settings.ADMINS,
    }

    return render(request, 'core/domain_info/domain_info.html', context)
