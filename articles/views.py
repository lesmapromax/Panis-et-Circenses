from django.utils import timezone

from django.views.generic import ListView, DetailView
from articles.models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    template_name = 'pages/article_list.html'
    context_object_name = 'articles_list'
    queryset = Article.objects.filter(is_published=True).order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ArticleView(DetailView):
    model = Article
    template_name = 'pages/article.html'
    context_object_name = 'article_view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
