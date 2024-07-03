from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Article


@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'body': request.POST['body']
        }
        Article.objects.create(**data).save()
    articles = Article.objects.all()
    return render(request, 'articles/index.html', context={'articles': articles})


@require_http_methods(['GET'])
def article_view(request, id):
    article = Article.objects.filter(pk=id).first()
    if not article:
        raise Http404()
    return render(request, 'articles/article.html', context={'article': article})