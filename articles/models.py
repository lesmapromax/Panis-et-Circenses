from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    cover = models.ImageField(upload_to='articles/static/articles/img/covers/%Y/%m/%d', null=True, blank=True)
    redactor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
