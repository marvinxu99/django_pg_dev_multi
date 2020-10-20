from django.db import models

from .code_value_set import CodeValueSet 


class CodeValue(models.Model):
    code_value = models.BigAutoField(primary_key=True, editable=False)
    definition = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    display = models.CharField(max_length=100)

    code_set = models.ForeignKey(CodeValueSet, related_name='cv_code_values', on_delete=models.CASCADE)

    active_ind = models.BooleanField("Active", default=True)
    active_dt_tm = models.DateTimeField(blank=True, null=True)
    # active_status_cd = models.IntegerField("Active Status")
    # active_status_dt_tm = models.DateTimeField("Active Status Date")

    begin_effective_dt_tm = models.DateTimeField('Begin Effective Date/Time', blank=True, null=True)
    end_effective_dt_tm = models.DateTimeField('End Effective Date/Time', blank=True, null=True)
    inactivate_dt_tm = models.DateTimeField(blank=True, null=True)
    display_sequence = models.IntegerField(default=0)
    
    # Winn Knowledge Index(WKI)
    wki = models.CharField("WKI", max_length=255, blank=True, null=True)
    concept_wki = models.CharField("Concept WKI", max_length=255, blank=True, null=True)
    wdf_meaning = models.CharField("Meaning", max_length=16, blank=True, null=True)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = "core_code_value"
        indexes = [
            models.Index(fields=['code_set'], name='cv_code_set_idx'),
            models.Index(fields=['display'], name='cv_display_idx'),
        ]

    def __str__(self):
        return self.display

