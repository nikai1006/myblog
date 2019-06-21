"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    URL配置文件
"""
from django.urls import path, re_path

# import blog.views as nikai
from . import views
from .api.myapi import SwaggerSchemaView

# 此处的app_name要和myblog种urls中的namespace保持一致
app_name = "blog"

urlpatterns = [
    path('myindex/', views.index),
    path('index/', views.index2),
    path('article/', views.getuser),
    path('articles/', views.getAll),
    path('article/<int:article_id>/', views.getPage, name='article_page'),
    path('update/<int:article_id>', views.edit_page, name='edit_page'),
    path('edit/action', views.edit_action, name='edit_action'),
    path('api/swagger', SwaggerSchemaView.get, name='get_json'),
    path('task/','', name='do')
]
