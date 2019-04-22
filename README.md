# myblog

#### 创建工程
```bash
django-admin startproject myblog
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

#### 运行
```bash
python manage runserver [ip:port]
```

#### 参考资料

- [django](https://docs.djangoproject.com/en/2.2/)
- [Django教程](http://www.runoob.com/django/django-first-app.html)