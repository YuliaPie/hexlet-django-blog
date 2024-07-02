from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse('article!')


def index(request, tags, article_id):
    context = {"tags": tags, "article_id": article_id}
    return render(request, 'article.html', context)
