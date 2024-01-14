from course_work.models.order import OrderItemInline
from .models import Article, Category, Item, Order, OrderItem, Promocode, Review
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from course_work.resource import ItemResource

@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["title", "content"]
    search_fields = ["title", "content"]

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    resource_class = ItemResource
    list_display = ["name", "price", "description", "category", "stock"]
    list_filter = ["category"]
    search_fields = ["name"]
    list_display_links = ["name"]

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "phone", "notes", "order_date", "used_promocode", "payment_amount", "payment_method", "delivery_method", "delivery_address", "get_item_list"]
    inlines = [OrderItemInline]
    list_filter = ["order_date", "payment_method", "delivery_method"]
    date_hierarchy = "order_date"
    search_fields = ["first_name", "last_name", "phone", "email", "notes", "used_promocode", "payment_amount", "delivery_address"]
    readonly_fields = ["order_date", "payment_amount", "get_item_list"]
    short_description = "Список товаров"

@admin.register(Promocode)
class PromocodeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["code", "discount_fixed", "discount_percent"]
    search_fields = ["code"]

@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ["customer", "rating", "product", "description", "review_date"]
    list_filter = ["review_date", "product", "rating"]
    date_hierarchy = "review_date"
    search_fields = ["customer", "description"]
    readonly_fields = ["review_date", "rating", "product", "customer", "description"]