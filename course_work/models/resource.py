from import_export import resources
from django.db import models
from django.contrib import admin
from simple_history.models import HistoricalRecords
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .item import Item

class ItemResource(resources.ModelResource):
 
    class Meta:
        model = Item
        fields = ('name', 'price', 'description', 'category', 'stock')
        export_order = ('name', 'price', 'description', 'category', 'stock')
        

    def get_export_queryset(self):
        return super().get_queryset().filter(stock__gt=0)

    def dehydrate_price(self, item):
        # Кастомизировать представление поля 'price'
        return str(item.price) + " USD"

    def get_name(self, instance):
        # Кастомизировать представление поля 'name'
        return instance.name.upper()
