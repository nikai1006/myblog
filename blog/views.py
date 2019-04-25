from django.shortcuts import render
from django.http import HttpResponse

from . import models


# Create your views here.
# 类似java的controller

def index(request):
    return HttpResponse('Hello,boy')


def getuser(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/index2.html', {'article': article})


def index2(request):
    return render(request, 'blog/index.html', {'xixi': 'This is first page'})


def getAll(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})


def getPage(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/home_page.html', {'article': article})


def edit_page(request):
    return render(request, 'blog/update.html')


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)
    return render(request, 'blog/home.html', {'articles': models.Article.objects.all()})
