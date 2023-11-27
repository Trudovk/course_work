from django.db import models
from .category import Category
from django.contrib import admin
from simple_history.models import HistoricalRecords
from simple_history.admin import SimpleHistoryAdmin


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    history = HistoricalRecords()

    def get_history(self):
        return ", ".join([f"{h.history_date} - {h.history_type}" for h in self.history.all()])

    def __str__(self):
        return self.name
    
    class Meta:
       verbose_name_plural = "Товары"
       verbose_name = "Товар"

@admin.register(Item)
class ItemAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ["name", "price", "description", "category", "stock"]
    list_filter = ["category"]
    search_fields = ["name"]
    list_display_links = ["name"]
