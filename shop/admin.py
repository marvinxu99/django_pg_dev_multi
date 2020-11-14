from django.contrib import admin

from .models import Product, Order, OrderItem, Payment


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


class PaymentInline(admin.StackedInline):   
    model = Payment
    can_delete = False
    verbose_name_plural = 'payments'
    fieldsets = (
        (None, {
            'fields': ['amount', ],
            'description': '*** Payment amount***'
        }),
        (None, {
            'fields': ['description', 'comment'],
        }),
    )
    extra = 0

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_id = request.user.user_id
        else:
            obj.updt_id = request.user.user_id
            obj.updt_cnt = obj.updt_cnt + 1 
        obj.save()


class OrderItemInLine(admin.StackedInline):
    model = OrderItem
    can_delete = True
    verbose_name_plural = 'Order Items'
    fieldsets = (
        (None, {
            'fields': ['product', 'quantity', 'price', 'discount', 'subtotal'],
        }),
        (None, {
            'fields': ['comment'],
        }),
    )
    extra = 0

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_id = request.user.user_id
            obj.subtotal = obj.price * obj.quantity - obj.discount
        else:
            obj.updt_id = request.user.user_id
            obj.subtotal = obj.price * obj.quantity - obj.discount
            obj.updt_cnt = obj.updt_cnt + 1 
        obj.save()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('total', 'quantity', 'description', 'owner', 'comment', 
                'create_dt_tm', 'create_id', 'updt_cnt', 'updt_dt_tm', 'updt_id')
    fields = [
        ('total'), 
        ('quantity'), 
        ('description'), 
        ('owner'), 
        ('comment')
    ]
    inlines = [ OrderItemInLine, PaymentInline ]
    ordering = ['-create_dt_tm', 'owner']

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.created_id = request.user.user_id
        else:
            obj.updt_id = request.user.user_id
            obj.updt_cnt = obj.updt_cnt + 1 
        obj.save()
