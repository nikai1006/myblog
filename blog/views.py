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
