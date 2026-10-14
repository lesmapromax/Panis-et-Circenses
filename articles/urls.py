from django.urls import path, URLPattern

import articles
from .views import Article

app_name = 'articles'
urlpatterns = [
    path('', Article.as_view(), name='articles')
]
