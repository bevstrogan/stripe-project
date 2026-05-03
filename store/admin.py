from django.contrib import admin

from store.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'id')
    search_fields = ('name', 'id',)
