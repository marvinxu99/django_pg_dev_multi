from django.db import models
from ..constants import ACTION_TYPE
from .transaction import Transaction

# Item Identifier
class TransAction(models.Model):
    """ Transaction Action
    ."""
    trans_action_id = models.BigAutoField(primary_key=True, editable=False)    

    action_dt_tm = models.DateTimeField(auto_now=True)  
    action_prsnl_id = models.BigIntegerField(default=0)
    action_type_cd = models.CharField("Action Type", max_length=2, 
                        choices = ACTION_TYPE.choices,
                        blank = False
                        )
    comment = models.TextField(blank=True, null=True)

    transaction =  models.ForeignKey(Transaction, related_name='Comments', on_delete=models.CASCADE)

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_applabel = models.CharField(max_length=20, default='0')

    class Meta:
        indexes = [
            models.Index(fields=['transaction_id',]),
        ]
        db_table = 'core_trans_comment'
        
    def __str__(self):
        """String for representing the Model object."""
        comment = self.comment[:20] 
        return comment



