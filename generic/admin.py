from django.contrib import admin
from .models import Category, Tag, Channel


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "cat_id"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "ch_id"]
    prepopulated_fields = {"slug": ("name",)}


