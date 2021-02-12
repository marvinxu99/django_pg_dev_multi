from django.contrib import admin

from ..models import Prsnl, Person_Alias, Prsnl_Alias


class PrsnlAliasInline(admin.StackedInline):
    model = Prsnl_Alias
    can_delete = False
    verbose_name_plural = 'prsnl alias'
    fieldsets = (
        (None, {
            'fields': ['alias', 'alias_expiry_dt_tm', 'alias_pool_cd'],
        }),
        (None, {
            'fields': ['is_active', 'active_status_cd'],
        }),
    )
    extra = 0


class PrsnlAdmin(admin.ModelAdmin):
    list_display = ('name_first', 'name_last', 'name_full_formatted', 'user', 'coloured_name', 'position', 'is_active')
    list_filter = ('is_active', )
    fieldsets = (
        (None, {'fields': ('name_first', 'name_middle', 'name_last', 'name_full_formatted')}),
        (None, {'fields': ('colour_code', )}),
        (None, {'fields': ('position', 'is_active', 'active_status_cd')}),
        (None, {
            'fields': ('user',),
            'description': 'Create or select a login username:'
        }),
    )
    search_fields = ['name_last', 'name_first']
    ordering = ['name_last',]
    verbose_name_plural = 'personnel'
    inlines = [ PrsnlAliasInline, ]

admin.site.register(Prsnl, PrsnlAdmin)
