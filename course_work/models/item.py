from django.db import models
from .category import Category
from django.contrib import admin
from simple_history.models import HistoricalRecords
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name
    
    class Meta:
       verbose_name_plural = "Товары"
       verbose_name = "Товар"

    


@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ["name", "price", "description", "category", "stock"]
    list_filter = ["category"]
    search_fields = ["name"]
    list_display_links = ["name"]
