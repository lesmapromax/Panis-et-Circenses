from django.conf.urls.static import static
from django.urls import path

from project import settings
from .views import ArticleListView, ArticleView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('article/<slug:slug>/', ArticleView.as_view(), name='article'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)