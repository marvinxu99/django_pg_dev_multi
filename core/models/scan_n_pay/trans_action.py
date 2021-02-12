from django.db import models
from ...constants import ACTION_TYPE, RESULT_STATUS, TRANSACTION_TYPE
from .trans_event import TransEvent

# Item Identifier
class Trans_Action(models.Model):
    """ Transaction Action
    ."""
    trans_action_id = models.BigAutoField(primary_key=True, editable=False)

    action_dt_tm = models.DateTimeField(auto_now=True)
    action_prsnl_id = models.BigIntegerField(default=0)
    action_type_cd = models.CharField("Action Type", max_length=2,
                        choices = ACTION_TYPE.choices,
                        blank = False
                        )

    client_id = models.BigIntegerField(default=0)
    person_id = models.BigIntegerField(default=0)

    comment = models.TextField(blank=True)

    event_id = models.BigIntegerField(default=0)    # its id should be the same id when the event was created.
    event_cd = models.IntegerField(default=0)
    event_class_cd = models.IntegerField(default=0)
    event_tag = models.CharField(max_length=255, blank=True)    # for display the event, e.g., "$34.56 <modified>"
    event_title = models.CharField(max_length=255, blank=True)

    result_status_cd = models.CharField("Result Status", max_length=2,
                        choices = RESULT_STATUS.choices,
                        default = RESULT_STATUS.ACTIVE
                        )

    trans_type_cd = models.CharField("Transaction Type", max_length=2,
                        choices = TRANSACTION_TYPE.choices,
                        default = TRANSACTION_TYPE.PURCHASE
                        )

    trans_event =  models.ForeignKey(TransEvent, related_name='Actions', on_delete=models.CASCADE)

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_applabel = models.CharField(max_length=20, default='0')

    class Meta:
        indexes = [
            models.Index(fields=['event_id',]),
        ]
        db_table = 'core_trans_action'

    def __str__(self):
        """String for representing the Model object."""
        comment = self.comment[:20]
        return comment
