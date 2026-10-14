from django.shortcuts import render
from django.views import View

class Article(View):
    def get(self, *args, **kwargs):
        context = {
            'title': 'Home',
        }
        return render(self.request, 'pages/article_list.html', context=context)

