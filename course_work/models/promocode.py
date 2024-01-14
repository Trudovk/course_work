from django.db import models
from django.contrib import admin
from simple_history.models import HistoricalRecords
from import_export.admin import ImportExportModelAdmin

class Promocode(models.Model):
    code = models.CharField(max_length=10)
    discount_fixed = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_percent = models.FloatField(max_length=1, blank=True, null=True)
    history = HistoricalRecords()
    class Meta:
       verbose_name_plural = "Промокоды"
       verbose_name = "Промокод"

