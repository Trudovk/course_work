from django.db import models
from django.contrib import admin

class Promocode(models.Model):
    code = models.CharField(max_length=10)
    discount_fixed = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_percent = models.FloatField(max_length=1, blank=True, null=True)
    class Meta:
       verbose_name_plural = "Промокоды"
       verbose_name = "Промокод"

@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ["code", "discount_fixed", "discount_percent"]
    search_fields = ["code"]