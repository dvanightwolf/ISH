from django.contrib import admin
from .models import Audio, AudioTag


# Register your models here.
class AudioTagAdmin(admin.StackedInline):
    model = AudioTag


@admin.register(Audio)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "audio", "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "description",)
    ordering = ("-created",)
    inlines = [AudioTagAdmin, ]
