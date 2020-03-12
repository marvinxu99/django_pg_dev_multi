from django.db import models

class CodeValue(models.Model):
    code_value = models.BigAutoField(primary_key=True, editable=False)
    code_set = models.IntegerField()
    definition = models.CharField(max_length=100)
    description = models.CharField(max_length=60)
    display = models.CharField(max_length=40)
    display_key = models.CharField(max_length=40)

    # is_active = models.BooleanField("Active")
    # active_dt_tm = models.DateTimeField()
    # active_status_cd = models.IntegerField("Active Status")
    # active_status_dt_tm = models.DateTimeField("Active Status Date")
    
    # wki = models.CharField("Winn Knowledge Index", max_length=255, blank=True, null=True)
    # concept_wki = models.CharField("Concept WKI", max_length=255, blank=True, null=True)

    update_appctx = models.IntegerField("Update Application Context", default=0)
    update_count = models.IntegerField("Update Application Context", default=1)
    update_dt_tm = models.DateTimeField("Date Updated", auto_now=True)
    update_id = models.IntegerField("Updated by", default=0)
    update_task = models.IntegerField(default=0)

    class Meta:
        db_table = "code_value"
        indexes = [
            models.Index(fields=['code_set'], name='code_set_idx'),
            models.Index(fields=['display_key'], name='display_key_idx'),
            # models.Index(fields=['first_name'], name='first_name_idx'),
        ]

    def __str__(self):
        return self.definition

