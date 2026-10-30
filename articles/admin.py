from django.contrib import admin
from .models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at', 'redactor', 'is_published']
    list_display_links = 'id', 'title'
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-updated_at',
    prepopulated_fields = {
        'slug': ('title',),
    }

admin.site.register(Article, ArticleAdmin)
