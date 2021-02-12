from django.db import models


# Items in the transaction(identified by event_id from the TransEvent)
class TransItem(models.Model):
    """ Items in a transaction event
    ."""
    trans_item_id = models.BigAutoField(primary_key=True, editable=False)

    event_id = models.BigIntegerField(default=0)

    item_id = models.BigIntegerField(default=0)
    item_identifier_id = models.BigIntegerField(default=0)
    item_price_id = models.BigIntegerField(default=0)
    item_discount_id = models.BigIntegerField(default=0)

    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    discountAmount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    price_final = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    comment =  models.CharField(max_length=255, blank=True)

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_applabel = models.CharField(max_length=20, default='0')

    class Meta:
        indexes = [
            models.Index(fields=['event_id',]),
            models.Index(fields=['item_id',]),
        ]
        db_table = 'core_trans_item'

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.description}, ${self.price_final}'
