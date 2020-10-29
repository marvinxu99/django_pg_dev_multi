from django.shortcuts import render

from ..models import Product
from core.models import CodeValue


def shop_home(request):
    """ Shop home
    """
    products = Product.objects.all()

    # code set 2(2) is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, "shop/shop_home.html", context)

