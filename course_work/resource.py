from import_export import resources
from django.db import models
from django.contrib import admin
from simple_history.models import HistoricalRecords
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Item

class ItemResource(resources.ModelResource):
 
    class Meta:
        model = Item
        fields = ('name', 'price', 'description', 'category', 'stock')
        export_order = ('name', 'price', 'description', 'category', 'stock')
        

    def get_export_queryset(self):
        return super().get_queryset().filter(stock__gt=0)
    
    def dehydrate_category(self, item):
        # Кастомизировать представление поля 'category'
        return item.category.name
    
    def dehydrate_stock(self, item):
        # Кастомизировать представление поля 'stock'
        return str(item.stock) + " шт."
    
    def dehydrate_price(self, item):
        # Кастомизировать представление поля 'price'
        return str(item.price) + " руб."

    def export_field(self, field, obj):
        return super().export_field(field, obj).lower()

    def get_export_headers(self):
        # Кастомизировать заголовки в русский 
        headers = super().get_export_headers()
        headers[0] = "Название"
        headers[1] = "Цена"
        headers[2] = "Описание"
        headers[3] = "Категория"
        headers[4] = "Количество"
        return headers
    
    
    
