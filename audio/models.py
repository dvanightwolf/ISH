from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from generic.models import Category, Tag


# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    audio = models.FileField(upload_to="audio/", blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_audio_url(self):
        return reverse('audio:audio_details', args=[self.id])


class AudioTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=False)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.tag.name + self.audio.title
