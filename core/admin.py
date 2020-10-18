from django.contrib import admin

# Register your models here.
from .models import (Item, ItemIdentifier, ItemBarcode, ItemPrice, ItemPriceHist, 
                    CodeValueSet, CodeValue)


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
    list_display = ('description', 'item_type_cd', 'active_status_cd', 'active_status_dt_tm',
                'create_dt_tm', 'create_id', 'updt_cnt', 'updt_dt_tm', 'updt_id')
    fields = [ 
        ('item_type_cd', 'description'), 
        ('active_status_cd', 'active_status_dt_tm')
    ]
    inlines = [ItemIdentifierInline, ItemBarcodeInline, ItemPriceInline]

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_id = request.user.user_id
        else:
            obj.updt_id = request.user.user_id
            obj.updt_cnt = obj.updt_cnt + 1 
        obj.save()


@admin.register(CodeValueSet)
class CodeSetValueAdmin(admin.ModelAdmin):
    list_display = ('code_set', 'display', 'description', 'definition', 'active_ind', 'cache_ind', 
                'change_access_ind', 'create_dt_tm', 'create_id', 'updt_cnt', 'updt_dt_tm', 'updt_id')
    fields = [ 
        ('display'), 
        ('description'), 
        ('definition'), 
        ('active_ind', 'cache_ind', 'change_access_ind',)
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_id = request.user.user_id
        else:
            obj.updt_id = request.user.user_id
            obj.updt_cnt = obj.updt_cnt + 1 
        obj.save()


@admin.register(CodeValue)
class CodeSetValueAdmin(admin.ModelAdmin):
    list_display = ('display', 'description', 'definition', 'code_set', 'active_ind', 
                'display_sequence', 'begin_effective_dt_tm', 'end_effective_dt_tm',
                'wki', 'concept_wki',
                'create_dt_tm', 'create_id', 'updt_cnt', 'updt_dt_tm', 'updt_id')
    fields = [ 
        ('code_set'),
        ('display'), 
        ('description'), 
        ('definition'), 
        ('active_ind'),
        ('begin_effective_dt_tm', 'end_effective_dt_tm'),
        ('wki', 'concept_wki'),
        ('display_sequence')
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_id = request.user.user_id
        else:
            obj.updt_id = request.user.user_id
            obj.updt_cnt = obj.updt_cnt + 1 
        obj.save()


