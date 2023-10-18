from django.urls import path

from .views import ArticleEslasticSearchView

urlpatterns = [
    path(
        "search/",
        ArticleEslasticSearchView.as_view({"get": "list"}),
        name="article_search",
    )
]
