from django.db import models
from django.conf import settings
from item_definition import ItemDefinition

# Product Identifier
class ProdIdentifier(models.Model):
    """ Item Itentifiers, such barcode
    ."""
    prod_identifier_id = models.BigAutoField(primary_key=True, editable=False)
    active_ind = models.BooleanField("Active", default=True)

    item = models.ForeignKey(ItemDefinition, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    parent_entity_id = models.IntegerField(default=0)
    parent_entity_name = models.CharField(max_length=100)
    
    prod_identifier_type_cd = models.IntegerField(default=0)

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
