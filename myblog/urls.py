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
from django.contrib import admin
from django.urls import path, include
from blog.api.myapi import SwaggerSchemaView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.permissions import AllowAny

# import blog.views as nikai
from blog import views as nikai


schema_view = get_schema_view(title='my API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
                              , permission_classes=())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('docs/', SwaggerSchemaView.as_view(), name='apiDocs'),
    path('docs/', schema_view, name='apiDocs'),
    path('index/', nikai.index),
    path('blog/', include('blog.urls', namespace='blog')),
    path('blog2/', include('blog2.urls')),

]
