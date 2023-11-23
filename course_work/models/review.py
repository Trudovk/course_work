from django.db import models
from .item import Item
from django.contrib import admin

class Review(models.Model):
    customer = models.CharField(max_length=100)
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=1)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    class Meta:
       verbose_name_plural = "Отзывы"
       verbose_name = "Отзыв"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["customer", "rating", "product", "description", "review_date"]
    list_filter = ["review_date", "product", "rating"]
    date_hierarchy = "review_date"
    search_fields = ["customer", "description"]
    readonly_fields = ["review_date", "rating", "product", "customer", "description"]