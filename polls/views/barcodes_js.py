
from django.shortcuts import render


def barcode_gen_js(request):
    '''
    Generate barcode at client side using jQuery and jquery-barcode.js
    '''
    try:
        if request.GET['code'] == '1d':
            bc_type = '1d'
        else:
            bc_type = '2d'
    except:
        bc_type = '2d'

    return render(request, 'polls/barcode_gen_js.html', { 'bc_type': bc_type})
