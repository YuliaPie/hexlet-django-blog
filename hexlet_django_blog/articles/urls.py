from django.urls import path
from hexlet_django_blog.articles.views import IndexView, ArticleView, ArticleFormCreateView


app_name = 'articles'

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
