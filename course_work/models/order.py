from django.db import models
from .item import Item
from .promocode import Promocode
from django.contrib import admin
from django.utils.html import format_html
from simple_history.models import HistoricalRecords
from import_export.admin import ImportExportModelAdmin

class PaymentMethodChoices(models.TextChoices):
    ON_PICKUP = "P", "При получении"
    ONLINE = "O", "Онлайн"

class DeliveryMethodChoices(models.TextChoices):
    PICKUP = "P", "Самовывоз"
    COURIER = "C", "Курьер"

class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=128)
    notes = models.TextField(blank=True, null=True)
    order_date = models.DateField(auto_now_add=True)
    used_promocode = models.CharField(max_length=10, blank=True, null=True)
    payment_amount = models.DecimalField(decimal_places=2, max_digits=9)
    payment_method = models.CharField(
        max_length=1, choices=PaymentMethodChoices.choices
    )

    delivery_method = models.CharField(
        max_length=1, choices=DeliveryMethodChoices.choices
    )
    delivery_address = models.TextField(blank=True, null=True)
    items = models.ManyToManyField(Item, through=OrderItem)
    history = HistoricalRecords()
    def get_item_list(self):
        return ", ".join([f"{p.item.name} - {p.quantity}" for p in self.orderitem_set.all()])
    class Meta:
        verbose_name_plural = "Заказы"
        verbose_name = "Заказ"

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    
@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "phone", "notes", "order_date", "used_promocode", "payment_amount", "payment_method", "delivery_method", "delivery_address", "get_item_list"]
    inlines = [OrderItemInline]
    list_filter = ["order_date", "payment_method", "delivery_method"]
    date_hierarchy = "order_date"
    search_fields = ["first_name", "last_name", "phone", "email", "notes", "used_promocode", "payment_amount", "delivery_address"]
    readonly_fields = ["order_date", "payment_amount", "get_item_list"]
    short_description = "Список товаров"