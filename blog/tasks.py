import djcelery, time,datetime

from celery.task import Task


class BlogTask(Task):
    name = 'blog-task'

    def run(self, *args, **kwargs):
        print('start task...')
        time.sleep(4)
        print('args={}, kwargs={}'.format(args, kwargs))
        print('end blog task')
        return datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S")
