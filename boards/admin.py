from django.contrib import admin

from .models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
#    list_filter = [ 'name' ]
    fields = ['name', 'description']
    search_fields = [ 'name' ]
    ordering = ['name']
