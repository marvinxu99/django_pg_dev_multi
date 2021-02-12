from django.shortcuts import render
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

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
        'page_title': _("All Products"),
    }

    return render(request, "shop/shop_home.html", context)


def get_products_by_category(request, prod_cat):
    """ Shop home
    """
    cv_cat = CodeValue.objects.filter(Q(code_set_id=2) & Q(active_ind=1) & Q(display=prod_cat))
    products = cv_cat[0].products.filter(active_ind=1)

    # code set 2(2) is Product Category
    categories = CodeValue.objects.filter(Q(code_set_id=2) & Q(active_ind=1)).order_by('display_sequence')

    context = {
        'products': products,
        'categories': categories,
        'page_title': prod_cat
    }

    return render(request, "shop/shop_home.html", context)
