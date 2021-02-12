from django.db import models
from .item import Item
from ...constants import ITEM_BARCODE_TYPE

# Item Identifier
class ItemBarcode(models.Model):
    """ Item Itentifiers, such barcode
    ."""
    item_barcode_id = models.BigAutoField(primary_key=True, editable=False)

    active_ind = models.BooleanField("Active", default=True)

    item = models.ForeignKey(Item, related_name='Barcodes', on_delete=models.CASCADE)

    parent_entity_id = models.IntegerField(default=0)
    parent_entity_name = models.CharField(max_length=100, blank=True)

    item_barcode_type_cd = models.CharField("Item Barcode Type",
                        max_length=2,
                        choices=ITEM_BARCODE_TYPE.choices,
                        default=ITEM_BARCODE_TYPE.BARCODE
                        )

    item_type_flag = models.IntegerField(default=0)

    primary_ind = models.BooleanField("Primary Code", default=True)
    sequence = models.IntegerField(default=0)

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_applabel = models.CharField(max_length=20, default='0')

    value = models.CharField(max_length=200)

    class Meta:
        indexes = [
            models.Index(fields=['item',]),
            models.Index(fields=['value',]),
        ]
        db_table = 'core_item_barcode'

    def __str__(self):
        """String for representing the Model object."""
        return f'Item ID ({self.item_barcode_type_cd}): {self.value}'
