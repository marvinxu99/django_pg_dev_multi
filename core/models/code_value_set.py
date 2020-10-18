from django.db import models

class CodeValueSet(models.Model):
    code_set = models.AutoField(primary_key=True, editable=False)

    display = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    definition = models.CharField(max_length=100)

    active_ind = models.BooleanField("Active", default=True)
    
    # Indicates whether this code set will be cached for system performance
    cache_ind = models.BooleanField("Cached", default=False)

    # True - allow end user to edit the code set
    change_access_ind = models.BooleanField("Change Allowed ", default=True)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = "core_code_value_set"
        indexes = [
            models.Index(fields=['code_set'], name='cvs_code_set_idx'),
            models.Index(fields=['display'], name='cvs_display_idx'),
        ]

    def __str__(self):
        return f'{self.display}({self.code_set})'

