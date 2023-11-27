from django.db import models
from django.contrib import admin
from simple_history.models import HistoricalRecords
from import_export.admin import ImportExportModelAdmin

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=32, unique=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.name
    class Meta:
       verbose_name_plural = "Категории"
       verbose_name = "Категория"

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]