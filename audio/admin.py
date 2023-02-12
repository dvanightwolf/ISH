from django.contrib import admin
from .models import Audio

# Register your models here.


@admin.register(Audio)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "audio", "tags", "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "description",)
    ordering = ("-created",)
