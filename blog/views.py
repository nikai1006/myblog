from django.http import HttpResponse
from django.shortcuts import render

from . import models
from .tasks import *
from django.http import JsonResponse

# Create your views here.
# 类似java的controller

HTTP_HOST = 'HTTP_HOST'


def index(request):
    print(request.path)

    meta_ = request.META
    if meta_ is not None:
        if HTTP_HOST in meta_:
            host_ = meta_[HTTP_HOST]
            print(host_)
        # for key in meta_:
        #     print(key + "=" + meta_[key])

    return HttpResponse(host_)


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


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/update.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/update.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id')
    if str(article_id) == '0':
        models.Article.objects.create(title=title, content=content)
        return render(request, 'blog/home.html', {'articles': models.Article.objects.all()})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/home.html', {'articles': models.Article.objects.all()})


def do(request):
    """
    任务
    :param request:
    :return:
    """
    print("start do task")
    BlogTask.delay()
    print("end do task")
    return JsonResponse({"result": "success"})
