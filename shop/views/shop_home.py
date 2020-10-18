from django.shortcuts import render

def shop_home(request):
    """ Shop home
    """

    return render(request, "shop/shop_home.html")

