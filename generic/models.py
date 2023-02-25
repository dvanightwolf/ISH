from django.db import models


# Create your models here.
class Category(models.Model):
    """A model that represents a category."""
    # Category name
    name = models.CharField(max_length=500, unique=True)
    # A field to make SEO friendly URLs
    slug = models.SlugField(max_length=1000)

    def __str__(self):
        """Makes a human readable representation of the category object in the admin site."""
        return self.name


class Tag(models.Model):
    """A model that represents a Tag."""
    # Tag name
    name = models.CharField(max_length=500, unique=True)
    # A field to make SEO friendly URLs
    slug = models.SlugField(max_length=1000)

    def __str__(self):
        """Makes a human readable representation of the category object in the admin site."""
        return self.name
