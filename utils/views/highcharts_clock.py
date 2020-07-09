from django.shortcuts import render
from ..forms import DictionaryForm

def highcharts_clock(request):
    return render(request, 'utils/highcharts_clock.html')
