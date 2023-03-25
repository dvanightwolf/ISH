from django.db import models


# Create your models here.
class Category(models.Model):
    """A model that represents a category."""
    choices = (('YouTube', 'YouTube'), ('Other', 'Other'))
    # Category name
    name = models.CharField(max_length=500)
    # Category ID.
    cat_id = models.CharField(max_length=1000, unique=True)
    # Category type.
    cat_type = models.CharField(max_length=100, blank=False, choices=choices, default="Other")
    # A field to make SEO friendly URLs
    slug = models.SlugField(max_length=1000)

    def __str__(self):
        """Makes a human readable representation of the category object in the admin site."""
        return self.name


class Channel(models.Model):
    # Category name
    name = models.CharField(max_length=500)
    # Category ID.
    ch_id = models.CharField(max_length=1000, unique=True)
    # A field to make SEO friendly URLs
    slug = models.SlugField(max_length=1000)


class Tag(models.Model):
    """A model that represents a Tag."""
    # Tag name
    name = models.CharField(max_length=500, unique=True)
    # A field to make SEO friendly URLs
    slug = models.SlugField(max_length=1000)

    def __str__(self):
        """Makes a human readable representation of the category object in the admin site."""
        return self.name
