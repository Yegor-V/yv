from django.urls import path

from .views import ArticlesListView

urlpatterns = [
    path('articles/', ArticlesListView.as_view(), name='articles_list'),
]
