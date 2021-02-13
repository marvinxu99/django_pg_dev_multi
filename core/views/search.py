from django.contrib.postgres.search import SearchQuery, SearchVector
from django.shortcuts import redirect, render


def search(request):
    try:
        search = str.split(request.GET['search'])
    except:
        search = ''
    return render(request, 'core/search.html', { 'search': search})
