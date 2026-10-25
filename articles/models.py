from django.db import models
from django.contrib.auth.models import User

import articles


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=400)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    cover = models.ImageField(upload_to='articles/static/articles/img/covers/%Y/%m/%d')
    redactor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self) -> str:
        return self.title