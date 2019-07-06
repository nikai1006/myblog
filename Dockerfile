FROM python:3.7.3
MAINTAINER nikai nikai.ni@klook.com

#RUN apt-get update \
#    && apt-get install -y --no-install-recommends \
#        postgresql-client \
#    && rm -rf /var/lib/apt/lists/*
#ENV TARGET="local"

WORKDIR /usr/src/app
#COPY requirements.txt ./
COPY . .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
RUN pip install https://github.com/darklow/django-suit/tarball/v2
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone #设置时区

EXPOSE 8000
ENTRYPOINT python manage.py runserver '0.0.0.0:8000' "$0"
CMD ["--settings=myblog.settings.docker"]