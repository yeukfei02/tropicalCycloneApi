from celery import Celery
from celery.schedules import crontab
import os

from app import app, db

from src.services.scrape_web import get_scrape_web_data
from src.models.TropicalCyclone import *

flask_env = os.environ.get('FLASK_ENV')
CELERY_BROKER_URL = ""
CELERY_RESULT_BACKEND = ""
if (flask_env == 'development'):
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
else:
    CELERY_BROKER_URL = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND = "redis://redis:6379/0"

def make_celery(app):
    app.config['CELERY_BROKER_URL'] = CELERY_BROKER_URL
    app.config['CELERY_RESULT_BACKEND'] = CELERY_RESULT_BACKEND
    app.config['CELERYBEAT_SCHEDULE'] = {
        # Executes every minute
        'periodic_task-every-minute': {
            'task': 'periodic_task',
            'schedule': crontab(minute="*")
        }
    }
    app.config['CELERY_TRACK_STARTED'] = True
    app.config['CELERY_SEND_EVENTS'] = True

    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask

    return celery

celery = make_celery(app)

@celery.task(name = "periodic_task")
def periodic_task():
    print(123123)
    get_scrape_web_data(TropicalCyclone, db)