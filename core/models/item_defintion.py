from django.db import models
from django.conf import settings


class ItemDefinition(models.Model):
    """ Parent table for all items
    ."""
    item_id = models.BigAutoField(primary_key=True, editable=False)

    active_ind = models.BooleanField("Active", default=True)
    active_status_cd = models.BigIntegerField(null=True, blank=True)
    active_status_dt_tm = models.DateTimeField(null=True, blank=True)
    active_status_prsnl_id = models.BigIntegerField(null=True, blank=True)

    approved_ind = models.BooleanField(default=false)

    item_type_cd = models.BigIntegerField(null=True, blank=True)
    reusable_ind = models.BooleanField("Reusable", default=False)
   
    batch_qty = models.BigIntegerField(null=True, blank=True)
    chargeable_ind = odels.BooleanField(default=True)
    component_ind = models.BooleanField(default=True)
    component_usage_ind = models.BooleanField(default=False)

    create_appctx = models.BigIntegerField(null=True, blank=True)
    create_dt_tm = models.DateTimeField(auto_now_add=True)
    create_id = models.BigIntegerField(null=True, blank=True)
    create_task = models.BigIntegerField(null=True, blank=True)

    inst_id = models.BigIntegerField(null=True, blank=True)

    item_level_flag = models.IntegerField(null=True, blank=True)
    latex_ind = models.BooleanField(default=False)

    temp_store_max = models.IntegerField(null=True, blank=True)
    temp_store_min = models.IntegerField(null=True, blank=True)
    temp_uom_cd = 


    shelf_life = models.IntegerField(null=True, blank=True)
    shelf_life_uom_cd = models.IntegerField('Shelf Life UOM', null=True, blank=True)

    updt_cnt = models.IntegerField(null=True, blank=True)
    updt_dt_tm = models.DateTimeField(null=True, blank=True)  
    updt_id = models.BigIntegerField(null=True, blank=True)
    updt_task = models.BigIntegerField(null=True, blank=True)
    updt_appctx = models.BigIntegerField(null=True, blank=True)
    
    
    


    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.item_id}'

