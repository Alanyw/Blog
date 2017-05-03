from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from article.models import Article


def index(request):
    return HttpResponse("Hello,world.You're at the article index")


def article_page(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except:
        None
    return render(request, 'article/article_page.html', {'article': article})
