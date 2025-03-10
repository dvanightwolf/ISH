from django.contrib import admin
from .models import Article, ArticleTag


# Register your models here.
class ArticleTagAdmin(admin.StackedInline):
    model = ArticleTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "content",)
    ordering = ("-created",)
    inlines = [ArticleTagAdmin, ]
