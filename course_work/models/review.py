from django.db import models
from .item import Item
from django.contrib import admin
from simple_history.models import HistoricalRecords
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

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
    history = HistoricalRecords()
    class Meta:
       verbose_name_plural = "Отзывы"
       verbose_name = "Отзыв"


