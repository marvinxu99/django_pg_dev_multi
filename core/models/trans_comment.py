from django.db import models
from .item import Item
from ..constants import TRANS_COMMENT_TYPE

# Item Identifier
class TransComment(models.Model):
    """ Transactions 
    ."""
    trans_comment_id = models.BigAutoField(primary_key=True, editable=False)    

    action_sequence = models.IntegerField(default=0)
    comment_dt_tm = models.DateTimeField(auto_now=True)  
    comment_prsnl_id = models.BigIntegerField(default=0)
    comment_type_cd = models.CharField("Comment Type", max_length=2, 
                        choices = TRANS_COMMENT_TYPE.choices,
                        blank = False
                        )
    comment = models.TextField(blank=True, null=True)

    display_mask = models.IntegerField(default=0)

    transaction_id = models.BigIntegerField(default=0)

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

        return self.comment[:20]
