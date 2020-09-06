celery worker -A app.celery --loglevel=info --purge
celery beat -A app.celery --loglevel=info