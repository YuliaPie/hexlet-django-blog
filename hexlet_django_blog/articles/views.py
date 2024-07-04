from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from hexlet_django_blog.articles.forms import ArticleForm
from hexlet_django_blog.articles.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('index') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})