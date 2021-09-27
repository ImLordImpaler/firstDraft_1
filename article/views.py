from django.shortcuts import render

from .models import Article

def articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles.html', context)