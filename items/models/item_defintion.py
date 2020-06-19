from django.db import models

# Create your models here.

    name_first = models.CharField("Fist Name", max_length=128, default='John')
    name_middle = models.CharField("Middle Name", max_length=128, blank=True, null=True)
    name_last = models.CharField("Last Name", max_length=128, default='Doe')
    name_full_formatted = models.CharField("Full Name", max_length=128, default='John Doe, MD')
    is_active = models.BooleanField("Active", default=True)
    active_status_cd = models.IntegerField("Active Status", default=1)
    active_status_dt_tm = models.DateTimeField("Active Status Date", auto_now_add=True)
    person_type_cd = models.IntegerField('User Type', default=1)
    
    created_dt_tm = models.DateTimeField("Date Created", null=True, blank=True)
    create_id = models.BigIntegerField('Created by', null=True, blank=True)

    updated_dt_tm = models.DateTimeField("Date Updated", null=True, blank=True)
    update_id = models.BigIntegerField('Updated by', null=True, blank=True)

class ItemDefinition(models.Model):
    """ Parent table for all items
    ."""
    item_id = models.BigAutoField(primary_key=True, editable=False)

    item_type_cd   
    
    reusable_ind = models.BooleanField("Reusable", default=True)
    
    active_ind = models.BooleanField("Active", default=True)

    active_status_cd = 
    active_status_dt_tm = models.DateTimeField("Ative Status Time", null=True, blank=True)
    active_status_prsnl_id = models.BigIntegerField('Active Status Updated by', null=True, blank=True)
    create_dt_tm = models.DateTimeField("Date Created", null=True, blank=True)
    create_id = models.BigIntegerField('Updated by', null=True, blank=True)
    create_task = models.BigIntegerField('Updated by', null=True, blank=True)
    create_applctx = models.BigIntegerField('Updated by', null=True, blank=True)
    updt_cnt = models.IntegerField('Updated Count', null=True, blank=True)
    updt_dt_tm = models.DateTimeField("Date Updated", null=True, blank=True)
    updt_id = models.BigIntegerField('Updated by', null=True, blank=True)
    updt_task = models.BigIntegerField('Update Task', null=True, blank=True)
    updt_applctx = models.BigIntegerField('Update App ', null=True, blank=True)
    component_ind = models.BooleanField("Component", default=True)
    shelf_life = models.IntegerField('Updated Count', null=True, blank=True)
    shelf_life_uom_cd = models.IntegerField('Updated Count', null=True, blank=True)
    component_usage_ind = 
    batch_qty
    approved_ind
    quickadd_ind
    unique_field
    substitution_ind
    latex_ind
    item_level_flag
    pha_type_flag
    logical_domain_id
    lot_tracking_ind
    multi_lot_transfer_ind
    component_trans_ind
    suppress_auto_fill_ind
    component_fill_return_ind
    pre_exp_date_uom_cd
    pre_exp_date_period_nbr
    chargeable_ind
    last_utc_ts
    implant_type_cd
    min_temp_amt
    max_temp_amt
    temp_uom_cd
    omf_success_ind
    updt_price_sched_price_ind
    udi_lot_nbr_ind
    udi_serial_nbr_ind
    udi_exp_date_ind
    udi_mfr_date_ind
    inst_id

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('catalog:author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

