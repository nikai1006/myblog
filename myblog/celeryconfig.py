import djcelery
from datetime import timedelta

djcelery.setup_loader()

CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    'work_queue': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    }
}

CELERY_DEFAULT_QUEUE = 'work_queue'

CELERY_IMPORTS = (
    'blog.tasks',
)

# 有些情况可以防止死锁
CELERY_FORCE_EXECV = True

# 深圳并发的worker数量
CELERYD_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行100个任务被销毁，可以防止内存泄露
CELERY_MAX_TASKS_PER_CHILD = 100

# 单个任务最大运行时间
CELERY_TASK_TIME_LIMIT = 12 * 30

CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'blog-task',# 此处配置tasks里面的name
        'schedule': timedelta(seconds=5),
        'options': {
            'queue': 'beat_tasks'
        }
    }
}
