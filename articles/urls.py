from django.urls import path, URLPattern

import articles
from .views import ArticleList, Article

app_name = 'articles'
urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('article/<int:id>/', Article.as_view(), name='article'),
]
