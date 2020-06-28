import uuid
from django.db import models
from .item import Item
from ..constants import ENTRY_MODE, TRANSACTION_TYPE

# Item Identifier
class Transaction(models.Model):
    """ Transactions 
    ."""
    transaction_id = models.BigAutoField(primary_key=True, editable=False)
    trans_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    active_ind = models.BooleanField("Active", default=True)
   
    client_id = models.BigIntegerField(default=0)

    trans_comment = models.ForeignKey(trans_comment, related_name='+', on_delete=models.CASCADE)

    coupon_used_ind = active_ind = models.BooleanField("Coupon Used", default=False)
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    entry_mode_cd = models.CharField("Entry Mode", max_length=2, 
                        choices = ENTRY_MODE.choices,
                        default = ENTRY_MODE.SCAN_N_PAY
                        )

    parent_entity_id = models.IntegerField(default=0)
    parent_entity_name = models.CharField(max_length=100, blank=True)
    
    sequence = models.IntegerField(default=0)

    trans_type = models.CharField("Transaction Type", max_length=2, 
                        choices = TRANSACTION_TYPE.choices,
                        default = TRANSACTION_TYPE.PURCHASE
                        )
    trans_dt_tm = models.DateTimeField(auto_now=True)  

    performed_dt_tm = models.DateTimeField(blank=True)  
    performed_prsnl_id = models.BigIntegerField(default=0)

    machine_id = models.BigIntegerField(default=0)

    total_quantity = models.IntegerField(default=0)
    total_orig_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_applabel = models.CharField(max_length=20, default='0')
    
    value = models.CharField(max_length=200)
    value_key = models.CharField(max_length=200)

    class Meta:
        indexes = [
            models.Index(fields=['item',]),
        ]
        db_table = 'core_item_identifier'
        
    def __str__(self):
        """String for representing the Model object."""
        return f'Item: {self.value}'
