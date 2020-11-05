from django.db import models

from shop.models import Cart
from shop.models import Product


# Shopping Cart Items
class CartItem(models.Model):
    """ items in shopping care
    ."""
    cart_item_id = models.BigAutoField(primary_key=True, editable=False)

    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    item = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
        
    comment =  models.CharField(max_length=255, blank=True)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'shop_cart_item'

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.product}({self.quantity})'