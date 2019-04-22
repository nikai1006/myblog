# myblog

#### 创建应用
1. 打开命令行，进入项目中manage.py同级目录
2. 命令行输入：python manage.py startapp blog
3. 添加应用名到settings.py中到INSTALLED_APPS中

#### 生成数据表
1.  打开命令行，进入项目中manage.py同级目录
2. 命令行输入：python manage.py makemigrations [app名]
3. 再执行python manage.py migrate

#### 参考资料

- [django](https://docs.djangoproject.com/en/2.2/)