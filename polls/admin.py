# Custom Admin Page:
# https://docs.djangoproject.com/en/3.0/intro/tutorial07/
from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """
    Using TabularInline (instead of StackedInline), the related objects
    are displayed in a more compact, table-based format:
    """
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    Replacing admin.site.register(Question) with the fillowing:
    You’ll follow this pattern – create a model admin class,
    then pass it as the second argument to admin.site.register() – any
    time you need to change the admin options for a model.
    """
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,  {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


# class PersonAliasInline(admin.TabularInline):
#     """
#     Using TabularInline (instead of StackedInline), the related objects
#     are displayed in a more compact, table-based format:
#     """
#     model = Person_Alias
#     extra = 2


# class PersonAdmin(admin.ModelAdmin):
#     """
#     Replacing admin.site.register(Question) with admin.site.register(Question, QuestionAdmin).
#     You’ll follow this pattern – create a model admin class,
#     then pass it as the second argument to admin.site.register() – any
#     time you need to change the admin options for a model.
#     """
#     list_display = ('name_first',
#                     'name_last',
#                     'name_full_formatted',
#                     'person_id',
#                     'person_type_cd',
#                     'is_active',
#                     'active_status_cd',
#                     'active_status_dt_tm',
#                     'created_dt_tm',
#                     )
#     list_filter = ['name_last', 'name_first']
#     search_fields = ['name_full_formatted']
#     inlines = [PersonAliasInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Person, PersonAdmin)
# admin.site.register(CodeValue)
