from django.db import models

from shop
# Order
class Order(models.Model):
    """ Stores items in shopping care
    ."""
    order_id = models.BigAutoField(primary_key=True, editable=False)

    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
        
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    comment =  models.CharField(max_length=255, blank=True)

    payment_id = models.ForeignKey(Payment, 
                                related_name='products',     # '+': Do not create backwards relation to this model 
                                on_delete=models.CASCADE,
                                limit_choices_to={'code_set': 2, 'active_ind': 1},
                                verbose_name="Category"
                            )

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['event_id',]),
            models.Index(fields=['item_id',]),
        ]
        db_table = 'core_trans_item'

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.description}, ${self.price_final}'