from django.db import models
from django.urls import reverse
from generic.models import Category, Tag


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    photo = models.ImageField(upload_to="article/", blank=True, null=True)    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_article_url(self):
        return reverse('article:article_details', args=[self.id])

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=False)

    def get_tag_url(self):
        return reverse('video:article_list', args=[self.tag.name])

    def __str__(self):
        return self.tag.name + self.article.title
