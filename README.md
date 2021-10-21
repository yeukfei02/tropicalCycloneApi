# tropicalCycloneApi

tropicalCycloneApi

documentation: <https://documenter.getpostman.com/view/3827865/TVCiSR7Z>

## Requirement

- install python(3.8)
- install pip3
- install celery
- install postgres
- install redis

## Testing and run

```zsh
// use requirements.txt
$ pip3 install -r requirements.txt

// run api
$ python3 app.py
or
$ flask run
or
$ gunicorn app:app --reload

// create db migration
$ python3 manage.py db init
$ python3 manage.py db migrate
$ python3 manage.py db upgrade

// run cron job
$ celery worker -A app.celery --loglevel=info --purge
$ celery beat -A app.celery --loglevel=info

// check schedule job in flower dashboard
$ flower -A app.celery --port=5555
open localhost:5555

// run test case
$ python3 src/test/main.test.py
```

## Docker

```zsh
// build images and start container in one line
docker-compose up -d --build

// go inside container
docker exec -it <containerId> /bin/bash

// check container logs
docker logs <containerId>

// remove and stop container
docker-compose down
```

open localhost:5000
