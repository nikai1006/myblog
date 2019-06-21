import djcelery, time

from celery.task import Task


class BlogTask(Task):

    def run(self, *args, **kwargs):
        print('start task...')
        time.sleep(4)
        print('args={}, kwargs={}'.format(args, kwargs))
        print('end blog task')
