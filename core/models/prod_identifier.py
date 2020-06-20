from django.db import models
from django.conf import settings
from .item_definition import ItemDefinition
from ..constants import PRODUCT_IDENTIFIER_TYPE

# Product Identifier
class ProdIdentifier(models.Model):
    """ Item Itentifiers, such barcode
    ."""
    prod_identifier_id = models.BigAutoField(primary_key=True, editable=False)
    active_ind = models.BooleanField("Active", default=True)

    item = models.ForeignKey(ItemDefinition, related_name='items', on_delete=models.CASCADE)
    
    parent_entity_id = models.IntegerField(default=0)
    parent_entity_name = models.CharField(max_length=100, blank=true)
    
    prod_identifier_type_cd = models.CharField(max_length=2, 
                        choices=PRODUCT_IDENTIFIER_TYPE.choices)

    prod_type_flag = models.IntegerField(default=0)

    primary_ind = models.BooleanField(default=False)
    sequence = models.IntegerField(default=0)

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now_add=True)  
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_appctx = models.BigIntegerField(default=0)
    
    value = models.CharField(max_length=200)
    value_key = models.CharField(max_length=200)

    class Meta:
        indexes = [
            models.Index(fields=['item_id',]),
        ]

    def __str__(self):
        """String for representing the Model object."""
        return f'Product ID({self.prod_identifier_type_cd}): {self.value}'
