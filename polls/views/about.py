from django.conf import settings
from django.shortcuts import render


def about(request):
    context = {
            'domain': settings.DOMAIN,
        }

    return render(request, 'polls/about.html', context)
