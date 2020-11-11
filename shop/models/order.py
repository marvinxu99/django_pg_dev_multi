from django.db import models
from django.conf import settings

from shop.models import Payment


# Order
class Order(models.Model):
    """ Stores items in shopping care
    ."""
    order_id = models.BigAutoField(primary_key=True, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='order', 
                            on_delete=models.SET_NULL, 
                            null=True, blank=True)

    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)       
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    payment = models.ForeignKey(Payment, 
                                related_name='order', 
                                on_delete=models.CASCADE,
                                verbose_name="Order"
                            )

    comment =  models.CharField(max_length=255, blank=True)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['payment',]),
        ]
        db_table = 'shop_order'

    def __str__(self):
        """String for representing the Model object."""
        return f'Order placed on { self.create_dt_tm.strftime("%d-%b-%Y") }, ${ self.total }'