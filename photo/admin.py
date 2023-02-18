from django.contrib import admin
from .models import Photo, PhotoTag


# Register your models here.
class PhotoTagAdmin(admin.StackedInline):
    model = PhotoTag


@admin.register(Photo)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "description",)
    ordering = ("-created",)
    inlines = [PhotoTagAdmin, ]
