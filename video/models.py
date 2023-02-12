from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from generic.models import Category


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    post_photo = models.ImageField(upload_to="video/", blank=False, null=False,
                                   default="Shiekh Ahmad Kuftaro.png")
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=False, null=False)
    video_time = models.IntegerField(blank=False, null=False)
    video_date = models.DateField(blank=False, null=False)
    size = models.IntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_video_url(self):
        return reverse('video:video_details', args=[self.id])
