from django.db import models
from django.contrib import admin

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
       verbose_name_plural = "Статьи"
       verbose_name = "Статья"

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
    search_fields = ["title", "content"]