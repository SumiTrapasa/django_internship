from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailtView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeletetView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailtView.as_view(), name='article-detail'),
    path('create/',ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeletetView.as_view(), name='article-delete'),
   

]

