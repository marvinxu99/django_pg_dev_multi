from django.contrib import admin

# Register your models here.
from .models import Item, ItemIdentifier, ItemBarcode, ItemPrice, ItemPriceHist


class ItemIdentifierInline(admin.TabularInline):
    model = ItemIdentifier
    fields = [ 
        ('active_ind', 'item_identifier_type_cd', 'value', 'value_key')
    ]
    extra = 1

class ItemBarcodeInline(admin.TabularInline):
    model = ItemBarcode
    fields = [
        ('active_ind', 'item_barcode_type_cd', 'value', 'primary_ind')
    ]
    extra = 1

class ItemPriceInline(admin.TabularInline):
    model = ItemPrice
    fields = [
        ('active_ind', 'price', 'effective_dt_tm', 'expiration_dt_tm')
    ]
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'item_type_cd', 'create_dt_tm', 'active_status_cd', 'active_status_dt_tm')
    fields = [ 
        ('item_type_cd', 'description'), 
        ('active_status_cd', 'active_status_dt_tm')
    ]

    inlines = [ItemIdentifierInline, ItemBarcodeInline, ItemPriceInline]

