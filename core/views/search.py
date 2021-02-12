from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import SearchQuery


def search(request):
    try:
        search = str.split(request.GET['search'])
    except:
        search = ''
    return render(request, 'core/search.html', { 'search': search})
