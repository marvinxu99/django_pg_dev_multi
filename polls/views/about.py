from django.shortcuts import render
from django.conf import settings


def about(request):
    context = {
            'domain': settings.DOMAIN,
        }

    return render(request, 'polls/about.html', context)
