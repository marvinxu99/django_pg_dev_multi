from django.shortcuts import render
from django.db.models import Q

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
        'page_title': "All Products"
    }

    return render(request, "shop/shop_home.html", context)


def get_product_by_category(request, prod_cat):
    """ Shop home
    """
    cv = CodeValue.objects.filter(Q(code_set_id=2) & Q(active_ind=1) & Q(display=prod_cat))
    products = cv[0].products.all()

    # code set 2(2) is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    context = {
        'products': products,
        'categories': categories,
        'page_title': prod_cat
    }

    return render(request, "shop/shop_home.html", context)

