from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'description', 'category_cd', 'active_ind', 
                'price', 'available', 'stock', 'image',
                'create_dt_tm', 'create_id', 'updt_cnt', 'updt_dt_tm', 'updt_id')
    fields = [
        ('name'), 
        ('display'), 
        ('description'), 
        ('category_cd'),
        ('active_ind'),
        ('price'),
        ('available', 'stock'), 
        ('image')
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_id = request.user.user_id
        else:
            obj.updt_id = request.user.user_id
            obj.updt_cnt = obj.updt_cnt + 1 
        obj.save()

