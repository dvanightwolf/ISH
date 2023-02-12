from django.contrib import admin
from .models import Photo

# Register your models here.


@admin.register(Photo)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "tags", "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "description",)
    ordering = ("-created",)
