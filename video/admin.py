from django.contrib import admin
from .models import Video, VideoTag


# Register your models here.
class VideoTagAdmin(admin.StackedInline):
    model = VideoTag


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail", "video_id", "video_date",
                    "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "description", "video_date",)
    ordering = ("-video_date",)
    inlines = [VideoTagAdmin, ]
