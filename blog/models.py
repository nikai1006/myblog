from django.db import models


# Create your models here.
# 类似java的DTO

class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)
