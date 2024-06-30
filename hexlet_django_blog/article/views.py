from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse('article!')


def index(request, tags, article_id):
    context = {"tags": tags, "article_id": article_id}
    return render(request, 'article.html', context)


"""
Сделайте так, чтобы hexlet_django_blog.article.views.index 
принимала строковый параметр "tags" и целочисленный параметр 
"article_id" из пути /articles/tags/article_id и выводила текст 
в виде Статья номер 42. Тег python
"""
