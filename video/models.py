from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from generic.models import Category, Tag


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    thumbnail = models.URLField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=True, null=True)
    video_id = models.CharField(blank=False, max_length=100, null=False)
    video_date = models.DateField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_video_url(self):
        return reverse('video:video_details', args=[self.id])

    def __str__(self):
        return self.title


class VideoTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.tag.name + self.video.title
