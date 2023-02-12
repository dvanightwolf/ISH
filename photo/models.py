from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from generic.models import Category


# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    photo = models.ImageField(upload_to="photo/", blank=False, null=False,
                              default="Shiekh Ahmad Kuftaro.png")
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_photo_url(self):
        return reverse('photo:photo_details', args=[self.id])
