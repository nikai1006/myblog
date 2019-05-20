# myblog

#### 创建工程
```bash
django-admin startproject myblog
```

#### 安装依赖
```bash
python3 -m pip install -r requirement.txt

国外仓库慢的话可以使用国内清华镜像仓库
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirement.txt
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
- 新建数据库
```mysql
CREATE DATABASE `myblog` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

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

#### 安装suit-2
```bash
pip uninstall django-suit
pip install https://github.com/darklow/django-suit/tarball/v2
```

#### 制作镜像
进入Dockerfile同级目录下，执行如下
```bash
 docker build -t myblog:1.0 .
```
- 启动
```bash
docker run --name tapd2 -p 18000:8000 -d myblog --settings=myblog.settings.local
```
- 初始化数据库
```bash
 docker exec -it tapd bash
 python manage.py makemigrations [app_names...] --settings=myblog.settings.local
 python manage.py migrate --settings=myblog.settings.local
```
#### 参考资料

- [django](https://docs.djangoproject.com/en/2.2/)
- [Django教程](http://www.runoob.com/django/django-first-app.html)
- [Django Path](https://www.cnblogs.com/polly-ling/p/9315645.html)
- [Python3.7安装mysqlclient](https://cloud.tencent.com/developer/article/1372417)
- [Django多环境配置](https://www.jianshu.com/p/ae85eac23f46)
- [rest_framework_swagger](https://www.jianshu.com/p/d7b614b85a74)
- [suit](https://django-suit.readthedocs.io/en/develop/getting_started.html)
- [sonar-scanner](https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner)
- [Sonar Webhooks](http://10.2.17.107:9000/documentation/project-administration/webhooks/)
- [django docker](https://github.com/ffreitasalves/django-boards)
- [entrypoint](https://yanbin.blog/pass-arguments-to-docker-container/#more-8608)
- [django-docker-demo](https://github.com/xander-ye/docker_test)
