from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import User as CustomUser
from ..models import Person, Prsnl
from ..forms import CustomUserCreationForm, CustomUserChangeForm

# The following are NOT NEEDED. leave them here for reference.
#
class PersonInline(admin.StackedInline):   
    model = Person
    can_delete = False
    verbose_name_plural = 'person'
    fieldsets = (
        (None, {
            'fields': ['name_first', 'name_middle', 'name_last', 'name_full_formatted'],
            'description': '***SKIP this section if it is for staff members.***'

        }),
        (None, {
            'fields': ['is_active', 'active_status_cd'],
        }),
    )
    extra = 0


class PrsnlInline(admin.StackedInline):   
    model = Prsnl
    can_delete = False
    verbose_name_plural = 'personnel'
    # fieldsets = (
    #     ('Names', {
    #         'fields': ['name_first', 'name_middle', 'name_last', 'name_full_formatted'],
    #         'classes': ['wide', 'extrapretty'],   # can be 'collapse', 'wide', 'extrapretty' 
    #         'description': 'this is needed'
    #     }),
    #     ('Advanced opitons', {
    #         'fields': ['is_active', 'active_status_cd'],
    #         'classes': ['wide', 'extrapretty']
    #     }),
    # )
    fieldsets = (
        (None, {
            'fields': ['name_first', 'name_middle', 'name_last', 'name_full_formatted'],
            'description': '***This section is ONLY needed for staff members.***'
        }),
        (None, {
            'fields': ['is_active', 'active_status_cd'],
        }),
    )
    extra = 0

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    # list_display = ('username', 'last_name', 'first_name', 'is_staff', 'is_active',)
    list_display = ('username', 'get_full_name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     (None, {'fields': ('is_staff', 'is_active')}),
    # )
    # # Special 'add_fieldsets" only works in UserAdmin
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide','extrapretty'),
    #         'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
    #     ),
    # )
    # search_fields = ('username',)
    ordering = ['-is_staff', 'username',]
    inlines = [ PersonInline, PrsnlInline]

admin.site.register(CustomUser, CustomUserAdmin)
