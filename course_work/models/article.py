from django.db import models
from django.contrib import admin
from simple_history.models import HistoricalRecords
from import_export.admin import ImportExportModelAdmin

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    history = HistoricalRecords()
    def __str__(self):
        return self.title
    class Meta:
       verbose_name_plural = "Статьи"
       verbose_name = "Статья"

