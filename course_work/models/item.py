from django.db import models
from .category import Category
from django.contrib import admin

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    class Meta:
       verbose_name_plural = "Товары"
       verbose_name = "Товар"

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "description", "category", "stock"]
    list_filter = ["category"]
    search_fields = ["name"]
    list_display_links = ["name"]
