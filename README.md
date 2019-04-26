# myblog

#### 创建工程
```bash
django-admin startproject myblog
```

#### 安装MySQL驱动
```bash
pip install mysqlclient
```

#### 创建应用
1. 打开命令行，进入项目中manage.py同级目录
2. 命令行输入：python manage.py startapp blog
3. 添加应用名到settings.py中到INSTALLED_APPS中

#### 生成数据表
[Model field refence](https://docs.djangoproject.com/en/1.10/ref/models/fields/)

#### 生成数据表
1.  打开命令行，进入项目中manage.py同级目录
2. 命令行输入：python manage.py makemigrations [app名]
3. 再执行python manage.py migrate
4. 执行python manage.py sqlmigrate 应用名 文件id 查看SQL语句

#### 页面呈现数据
1. views.py中import models
2. article = models.Article.objects.get(pk=0)

#### 配置Admin
- 创建用户 
```bash
python manage.py createsuperuser
```
创建了一个超级用户

#### 修改数据默认显示名称
1. 在Article类下面添加一个方法
2. Python3：`__str__(self)` \
   python2.7: `__unicode__(self)`
3. return self.title


#### Django中的超链接
超链接目标地址
1. href后面是`目标地址`
2. template中用 target-url 'app_name:url_name' param ,其中app_name和url_name都在url中配置



#### django shell
```bash
python manage.py shell
```


#### 运行
```bash
python manage runserver [ip:port]
```
#### 多环境下运行指定环境
```bash
python manage.py runserver --settings=myblog.settings.base
python manage.py runserver --settings=myblog.settings.local
python manage.py runserver --settings=myblog.settings.prd
python manage.py runserver --settings=myblog.settings.test
```

#### 参考资料

- [django](https://docs.djangoproject.com/en/2.2/)
- [Django教程](http://www.runoob.com/django/django-first-app.html)
- [Django Path](https://www.cnblogs.com/polly-ling/p/9315645.html)
- [Python3.7安装mysqlclient](https://cloud.tencent.com/developer/article/1372417)
- [Django多环境配置](https://www.jianshu.com/p/ae85eac23f46)
