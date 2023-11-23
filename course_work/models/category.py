from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.name
    class Meta:
       verbose_name_plural = "Категории"
       verbose_name = "Категория"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]