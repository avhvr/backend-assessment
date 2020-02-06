import logging
from celery import Celery

logger = logging.getLogger("default")


def make_celery(application):
    celery = Celery(
        application.import_name,
        broker=application.config['CELERY_SETTINGS']['BROKER'])
    celery.conf.update(application.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with application.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

        def on_failure(self, exc, task_id, args, kwargs, einfo):
            logger.debug(f"{task_id} FAILED: {exc} {args} {kwargs} {einfo}")

    celery.Task = ContextTask

    return celery
