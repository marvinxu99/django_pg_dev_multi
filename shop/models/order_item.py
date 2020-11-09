from django.db import models

from shop.models import Order
from shop.models import Product


# Shopping Cart Items
class OrderItem(models.Model):
    """ items in an order
    ."""
    order_item_id = models.BigAutoField(primary_key=True, editable=False)

    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)

    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # price = item_price * quantity

    comment =  models.CharField(max_length=255, blank=True)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'shop_order_item'
        ordering = ('product', )


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.product}({self.quantity})'