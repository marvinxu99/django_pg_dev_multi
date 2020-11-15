from django.db import models
from django.conf import settings

from core.constants import CODE_SET
from core.models import CodeValue

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

    comment =  models.CharField(max_length=255, blank=True)

    active_ind = models.BooleanField("Active", default=True)
    order_status = models.ForeignKey(CodeValue, 
                            related_name='+',     # '+': Do not create backwards relation to this model 
                            on_delete=models.CASCADE,
                            limit_choices_to={'code_set': CODE_SET.ORDER_STATUS, 'active_ind': 1},
                            verbose_name="Order Status"
                        )
 

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['description',]),
        ]
        db_table = 'shop_order'

    def __str__(self):
        """String for representing the Model object."""
        return f'Order placed on { self.create_dt_tm.strftime("%d-%b-%Y") }, ${ self.total }'