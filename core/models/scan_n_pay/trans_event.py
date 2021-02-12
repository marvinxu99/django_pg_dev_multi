import uuid
import pytz
from django.db import models
from ...constants import ENTRY_MODE, TRANSACTION_TYPE, RESULT_STATUS
from datetime import datetime


# Item Identifier
class TransEvent(models.Model):
    """ Transactions
    ."""
    trans_event_id = models.BigAutoField(primary_key=True, editable=False)
    trans_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Determines whether the information stored in the record has been authenticated.
    # 1: if event_status=authenticated, modified, or superseded; 0: for all others.
    authentic_flag = models.IntegerField(default=1)

    client_id = models.BigIntegerField(default=0)
    person_id = models.BigIntegerField(default=0)

    coupon_used_ind = models.BooleanField("Coupon Used", default=False)
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    entry_mode_cd = models.CharField("Entry Mode", max_length=2,
                        choices = ENTRY_MODE.choices,
                        default = ENTRY_MODE.SCAN_N_PAY
                        )
    parent_entity_id = models.BigIntegerField(default=0)
    parent_entity_name = models.CharField(max_length=100, blank=True)

    performed_dt_tm = models.DateTimeField(blank=True)
    performed_prsnl_id = models.BigIntegerField(default=0)


    sequence = models.IntegerField(default=0)

    trans_comment_ind = models.BooleanField("Active", default=False)

    # It represents the actual result date time
    trans_end_dt_tm = models.DateTimeField(auto_now=True)
    trans_start_dt_tm = models.DateTimeField(blank=True)

    event_cd = models.IntegerField(default=0)
    event_class_cd = models.IntegerField(default=0)
    # event_id is a unique identifier for an event.  Uniquely identifies a logical clinical event row.
    # There may be more than one row with the same event_id, but only one of those
    # rows will be current as indicated by the valid_until_dt_tm field.
    event_id = models.BigIntegerField(default=0)                           # its id should be the same id when the event was created.
    event_tag = models.CharField(max_length=255, blank=True, null=True)    # for display the event, e.g., "$34.56 <modified>"
    event_title = models.CharField(max_length=255, blank=True, null=True)

    result_status_cd = models.CharField("Result Status", max_length=2,
                        choices = RESULT_STATUS.choices,
                        default = RESULT_STATUS.ACTIVE
                        )

    trans_type_cd = models.CharField("Transaction Type", max_length=2,
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
    verified_dt_tm = models.DateTimeField(blank=True, null=True)
    verified_prsnl_id = models.BigIntegerField(default=0)

    workstation_id = models.BigIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['performed_dt_tm',]),
            models.Index(fields=['person_id',]),
            models.Index(fields=['event_id',]),
            models.Index(fields=['performed_prsnl_id',]),
            models.Index(fields=['trans_end_dt_tm',]),
        ]
        db_table = 'core_trans_event'

    # def save(self, *args, **kwargs):
    #     # do something
    #     super(TransEvent, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return f'Item: {self.event_tag}'
