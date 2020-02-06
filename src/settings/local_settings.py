import os


DEBUG = True
LOG_ROOT = os.environ.get("LOG_ROOT")
LOG_FILENAME = "{}.log".format(os.environ.get("APPLICATION_NAME"))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'encoding': 'utf-8',
            'filename': os.path.join(LOG_ROOT, LOG_FILENAME)
        }
    },
    'loggers': {
        'default': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propogate': True,
        }
    }
}


MONGO_SETTINGS = {
    'DB_NAME': os.environ.get('DB_NAME'),
    'DB_HOST': os.environ.get('DB_HOST'),
    'DB_PORT': int(os.environ.get('DB_PORT', 27017)),
    'DB_USERNAME': os.environ.get('DB_USERNAME'),
    'DB_PASSWORD': os.environ.get('DB_PASSWORD'),
}

CELERY_SETTINGS = {
    'BROKER' : f"{os.environ.get('DB_TRANSPORT')}://{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}",
}

CELERY_RESULT_BACKEND = os.environ.get('DB_TRANSPORT')
CELERY_MONGODB_BACKEND_SETTINGS = {
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'database': os.environ.get('DB_NAME'),
    'taskmeta_collection': os.environ.get('DB_TASK_COLLECTION'),
}
