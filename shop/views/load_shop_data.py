from django.shortcuts import render
from django.conf import settings
import json
import os
import requests
from urllib.request import urlretrieve
from urllib.parse import urlparse
from django.core.files import File
from django.contrib.auth.decorators import permission_required

from ..models import Product
from core.models import CodeValue


@permission_required('product.can_load_shop_data')
def load_shop_data(request):
    ''' Load json data from shop/fixtures/shop_data.json
    '''
    f_path = os.path.join(settings.BASE_DIR, 'shop', 'fixtures')
    f_name = "shop_data"
    json_file = os.path.join(f_path, f_name + '.json')
    with open(json_file) as f:
        data = json.load(f)

    for key in data:
        category_id = data[key]['id']
        for i in range(len(data[key]['items'])):
            product = Product()
            product.category_cd_id = category_id
            product.display = data[key]['items'][i]['name']
            product.name = data[key]['items'][i]['name']
            product.description = data[key]['items'][i]['name']
            product.price = data[key]['items'][i]['price']
            product.available = True
            product.stock = 20
            product.save()

            # get the images, e.g., 'https://i.ibb.co/xJS0T3Y/camo-vest.png'
            img_url = data[key]['items'][i]['imageUrl']
            f_name = urlparse(img_url).path.split('/')[-1]
            content = urlretrieve(img_url)
            product.image.save(f_name, File(open(content[0], mode='rb')), save=True)
           
    products = Product.objects.all()

    # code set 2 is Product Category
    categories = CodeValue.objects.filter(code_set_id=2).order_by('display_sequence')

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, "shop/shop_home.html", context)
