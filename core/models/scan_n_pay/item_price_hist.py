from django.db import models
from django.utils import timezone
from .item import Item
from .item_price import ItemPrice
from ...constants import ACTIVE_STATUS, ITEM_PRICE_TYPE


# Item price history
class ItemPriceHist(models.Model):
    """ Item Itentifiers, such barcode
    """
    item_price_hist_id = models.BigAutoField(primary_key=True, editable=False)

    active_ind = models.BooleanField("Active", default=True)
    active_status_cd = models.CharField(max_length=2,
                                        choices=ACTIVE_STATUS.choices,
                                        default=ACTIVE_STATUS.ACTIVE
                                        )
    active_status_dt_tm = models.DateTimeField(null=True, blank=True)
    active_status_prsnl_id = models.BigIntegerField(default=0, blank=True)

    contract_description = models.CharField(max_length=100)
    contract_id = models.BigIntegerField(default=0)
    contract_line_id = models.BigIntegerField(default=0)
    contract_nbr = models.CharField(max_length=40, blank=True)
    contract_type = models.CharField(max_length=100, blank=True)
    contributor_system_cd = models.BigIntegerField(default=0)

    create_applabel = models.CharField(max_length=20, blank=True)
    create_dt_tm = models.DateTimeField(default=timezone.now)
    create_id = models.BigIntegerField(default=0)
    create_task = models.BigIntegerField(default=0)

    effective_dt_tm = models.DateTimeField(auto_now_add=True)
    expiration_dt_tm = models.DateTimeField(null=True, blank=True)

    fixed_price_ind = models.BooleanField("Price Fixed", default=True)

    item = models.ForeignKey(Item, related_name='+', on_delete=models.CASCADE)
    item_price = models.ForeignKey(ItemPrice, related_name='+', on_delete=models.CASCADE)

    min_order_quantity = models.BigIntegerField(default=0)
    order_qty_multiple = models.IntegerField(default=0)

    organization_id = models.BigIntegerField(default=0)
    package_type_id = models.BigIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_quote_source = models.CharField(max_length=100, blank=True)
    price_type_cd = models.CharField(max_length=2,
                                        choices=ITEM_PRICE_TYPE.choices,
                                        default=ITEM_PRICE_TYPE.QUOTE)

    updt_cnt = models.IntegerField(default=0)
    updt_dt_tm = models.DateTimeField(auto_now=True)
    updt_id = models.BigIntegerField(default=0)
    updt_task = models.BigIntegerField(default=0)
    updt_applabel = models.CharField(max_length=20, blank=True)

    vendor_price_schedule_id = models.BigIntegerField(default=0)


    class Meta:
        indexes = [
            models.Index(fields=['item',]),
            models.Index(fields=['item_price',]),
            models.Index(fields=['contract_line_id',]),
            models.Index(fields=['organization_id',]),
            models.Index(fields=['package_type_id',]),
        ]
        db_table = "core_item_price_hist"

    def __str__(self):
        """String for representing the Model object."""
        return f'item id ({item.item_id}): price history. '
