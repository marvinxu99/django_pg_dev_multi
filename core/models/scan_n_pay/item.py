import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from ...constants import ACTIVE_STATUS, UOM_TEMP, UOM_SHELF_LIFE, ITEM_TYPE

class Item(models.Model):
    """ Parent table for all items
    ."""
    item_id = models.BigAutoField(primary_key=True, editable=False)
    item_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    active_ind = models.BooleanField("Active", default=True)
    active_status_cd = models.CharField("Active Status", max_length=2,
                                        choices=ACTIVE_STATUS.choices,
                                        default=ACTIVE_STATUS.ACTIVE
                                        )
    active_status_dt_tm = models.DateTimeField(default=timezone.now)
    active_status_prsnl_id = models.BigIntegerField(default=0)

    approved_ind = models.BooleanField(default=False)

    item_type_cd = models.CharField("Item Type", max_length=2,
                                    choices=ITEM_TYPE.choices,
                                    default=ITEM_TYPE.GENERAL
                                    )

    reusable_ind = models.BooleanField("Reusable", default=False)

    batch_quantity = models.BigIntegerField(default=0)
    chargeable_ind = models.BooleanField(default=True)
    component_ind = models.BooleanField(default=True)
    component_usage_ind = models.BooleanField(default=False)

    create_applabel = models.CharField(max_length=20, default='0')
    create_dt_tm = models.DateTimeField(default=timezone.now)
    create_id = models.BigIntegerField(default=0)
    create_task = models.BigIntegerField(default=0)

    description = models.CharField(max_length=40)

    inst_id = models.BigIntegerField(default=0)

    item_level_flag = models.IntegerField(null=True, blank=True)
    latex_ind = models.BooleanField(default=False)

    temp_store_max = models.IntegerField(null=True, blank=True)
    temp_store_min = models.IntegerField(null=True, blank=True)
    temp_uom_cd = models.CharField(max_length=1,
                                    choices=UOM_TEMP.choices,
                                    default=UOM_TEMP.DEGC
                                )

    shelf_life = models.IntegerField(null=True, blank=True)
    shelf_life_uom_cd = models.CharField("Shelf Life UOM", max_length=1,
                                choices=UOM_SHELF_LIFE.choices,
                                default=UOM_SHELF_LIFE.HOURS
                                )

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_applabel = models.CharField(max_length=20, default='0')

    class Meta:
        indexes = [
            models.Index(fields=['item_type_cd',]),
            models.Index(fields=['updt_dt_tm',]),
        ]

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.item_id}'
