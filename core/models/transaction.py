import uuid
import pytz
from django.db import models
from ..constants import ENTRY_MODE, TRANSACTION_TYPE
from datetime import datetime

# Item Identifier
class Transaction(models.Model):
    """ Transactions 
    ."""
    transaction_id = models.BigAutoField(primary_key=True, editable=False)
    trans_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    client_id = models.BigIntegerField(default=0)
    coupon_used_ind = models.BooleanField("Coupon Used", default=False)
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    entry_mode_cd = models.CharField("Entry Mode", max_length=2, 
                        choices = ENTRY_MODE.choices,
                        default = ENTRY_MODE.SCAN_N_PAY
                        )
    parent_entity_id = models.IntegerField(default=0)
    parent_entity_name = models.CharField(max_length=100, blank=True)
    
    performed_dt_tm = models.DateTimeField(blank=True)  
    performed_prsnl_id = models.BigIntegerField(default=0)
    person_id = models.BigIntegerField(default=0)

    sequence = models.IntegerField(default=0)

    trans_comment_ind = models.BooleanField("Active", default=False)

    trans_dt_tm = models.DateTimeField(auto_now=True)  
    trans_event_tag = models.DateTimeField(auto_now=True)    # for display the event, e.g., "$34.56 <modified>"
    trans_event_title = models.DateTimeField(auto_now=True)  
    trans_type = models.CharField("Transaction Type", max_length=2, 
                        choices = TRANSACTION_TYPE.choices,
                        default = TRANSACTION_TYPE.PURCHASE
                        )
    
    total_quantity = models.IntegerField(default=0)
    total_orig_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_applabel = models.CharField(max_length=20, default='0')

    valid_from_dt_tm = models.DateTimeField(auto_now_add=True)
    valid_until_dt_tm = models.DateTimeField(default=datetime(2150,12,31,0,0, tzinfo=pytz.UTC)) 

    workstation_id = models.BigIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['performed_dt_tm',]),
            models.Index(fields=['person_id',]), 
            models.Index(fields=['performed_prsnl_id',]), 
            models.Index(fields=['trans_dt_tm',]),
        ]
        db_table = 'core_transaction'
        
    def __str__(self):
        """String for representing the Model object."""
        return f'Item: {self.trans_event_tag}'
