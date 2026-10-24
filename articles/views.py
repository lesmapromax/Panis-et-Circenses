from django.shortcuts import render
from django.views import View

class ArticleList(View):
    def get(self, *args, **kwargs):
        context = {
            'title': 'Home',
        }
        return render(self.request, 'pages/article_list.html', context=context)


class Article(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'pages/article.html')