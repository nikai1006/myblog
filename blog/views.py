from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 类似java的controller

def index(request):
    return HttpResponse('Hello,boy')