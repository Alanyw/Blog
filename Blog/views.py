from django.shortcuts import render

from article.models import Article


def index(request):
    latest_article_list = Article.objects.order_by("pub_date")[::-1]
    title = Article.objects.order_by("title")
    context = {
        'latest_article_list': latest_article_list,
        'title': title,
    }
    return render(request, 'Blog/index.html', context)
