from django.db import models

class CodeValueSet(models.Model):
    code_set = models.IntegerField(default=0)

    definition = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    display = models.CharField(max_length=100)

    active_ind = models.BooleanField("Active", default=True)

    change_access_ind = models.BooleanField("Change Allowed ", default=True)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = "core_code_value_set"
        indexes = [
            models.Index(fields=['code_set'], name='code_set_idx'),
            models.Index(fields=['display'], name='display_idx'),
        ]

    def __str__(self):
        return self.definition

