from django.db import models
from .item import Item
from ...constants import ITEM_IDENTIFIER_TYPE

# Item Identifier
class ItemIdentifier(models.Model):
    """ Item Itentifiers, such brand name, description, generic name, etc.
        Barcode is stored in item_barcode table
    ."""
    item_identifier_id = models.BigAutoField(primary_key=True, editable=False)

    active_ind = models.BooleanField("Active", default=True)

    item = models.ForeignKey(Item, related_name='Identifiers', on_delete=models.CASCADE)

    parent_entity_id = models.IntegerField(default=0)
    parent_entity_name = models.CharField(max_length=100, blank=True)

    item_identifier_type_cd = models.CharField("Item Identifier Type", max_length=2,
                        choices=ITEM_IDENTIFIER_TYPE.choices,
                        default=ITEM_IDENTIFIER_TYPE.DESCRIPTION
                        )

    item_type_flag = models.IntegerField(default=0, blank=True)

    primary_ind = models.BooleanField(default=False)
    sequence = models.IntegerField(default=0)

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_applabel = models.CharField(max_length=20, default='0')

    value = models.CharField(max_length=200)
    value_key = models.CharField(max_length=200)

    class Meta:
        indexes = [
            models.Index(fields=['item',]),
        ]
        db_table = 'core_item_identifier'

    def __str__(self):
        """String for representing the Model object."""
        return f'Item: {self.value}'
