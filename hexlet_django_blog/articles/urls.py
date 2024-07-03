from django.urls import path
from hexlet_django_blog.articles import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.article_view, name='article'),
]
