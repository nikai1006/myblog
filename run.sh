#!/bin/bash

#sed是一个Linux编辑器吧，此命令的作用是查找文件/etc/nginx/nginx.conf中包含user的行，并将此行的nginx替换成root
sed -i '/user/{s/nginx/root/}' /etc/nginx/nginx.conf
#将项目nginx配置连接到nginx配置
ln -s /root/project/mysite_nginx.conf /etc/nginx/conf.d/
#启动nginx
nginx
#赋予wait-for-it.sh可执行权限
chmod u+x wait-for-it.sh
#判断数据库端口是否可用，因为数据库未准备好的话接下来的数据库刷新操作将失败。
#其实，假如我们事先启动好了一个数据库容器的话，此操作也可以省略。
#这样做是因为最后我们会使用docker-compose来一起管理两个或者多个容器，
#docker-compose里面三个关键字：link、depends_on、volume_from是可以确定容器的启动顺序的，
#但是，容器里面的mysql是否启动那就不一定了，所以我们检测下端口比较稳妥。
#没有好我们等几秒也无妨
#另外，这里的两个环境变量DB_PORT_3306_TCP_ADDR和DB_PORT_3306_TCP_PORT是mysql容器中的，
#不用猜也知道，一个是host，一个是port
#如果我们通过link将一个容器连接到mysql容器，mysql容器中的一些环境变量会共享出来的。
./wait-for-it.sh $DB_PORT_3306_TCP_ADDR:$DB_PORT_3306_TCP_PORT &
wait

#设置manage.py中使用的setting
export DJANGO_SETTINGS_MODULE=myblog.settings.mysql

#进入mysite目录（application下一级目录，不是mysite目录下的mysite）
#刚开始也许你有点困惑，不知道现在操作的目录到底在哪里，不像通常操作Linux，我可以pwd一下。
#其实是这样的，你以此脚本所在的位置为参照，你看项目目录结构发现，
#start_script与目录mysite是同一级的，manage.py在mysite之下，对吧
cd myblog
#刷新数据库
./manage.py migrate --noinput
#加载管理员用户到数据库，以便容器启动之后不必再进入容器执行python manage.py createsuperuser操作
./manage.py loaddata ./fixtures/superuser.json
#收集静态文件
./manage.py collectstatic --noinput

#返回上级目录，myblog_uwsgi.ini所在的目录
cd ..
#启动uwsgi
uwsgi --ini myblog_uwsgi.ini