from django.db import models

class CodeValue(models.Model):
    code_value = models.BigAutoField(primary_key=True, editable=False)
    definition = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    display = models.CharField(max_length=100)

    code_set = models.IntegerField(default=0)

    active_ind = models.BooleanField("Active", default=True)
    active_dt_tm = models.DateTimeField(blank=True, null=True)
    # active_status_cd = models.IntegerField("Active Status")
    # active_status_dt_tm = models.DateTimeField("Active Status Date")

    begin_effective_dt_tm = models.DateTimeField(blank=True)
    end_effevtive_dt_tm = models.DateTimeField(blank=True)
    inactivate_dt_tm = models.DateTimeField(blank=True)
    display_sequence = models.IntegerField(default=0)
    
    wki = models.CharField("Winn Knowledge Index", max_length=255, blank=True, null=True)
    concept_wki = models.CharField("Concept WKI", max_length=255, blank=True, null=True)

    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(default=0)
    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)  
    updt_id = models.BigIntegerField(default=0)

    class Meta:
        db_table = "core_code_value"
        indexes = [
            models.Index(fields=['code_set'], name='code_set_idx'),
            models.Index(fields=['display'], name='display_idx'),
            # models.Index(fields=['first_name'], name='first_name_idx'),
        ]

    def __str__(self):
        return self.definition

