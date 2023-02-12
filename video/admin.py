from django.contrib import admin
from .models import Video

# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "post_photo", "video_url", "tags", "video_time", "video_date",
                    "size", "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "description", "video_date",)
    ordering = ("-video_date",)
