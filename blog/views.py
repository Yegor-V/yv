from django.views.generic import ListView

from .models import Article


class ArticlesListView(ListView):
    model = Article
    template_name = 'blog/articles.html'
