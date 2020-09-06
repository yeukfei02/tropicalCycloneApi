# tropicalCycloneApi

tropicalCycloneApi

documentation: https://documenter.getpostman.com/view/3827865/TVCiSR7Z

## Requirement:
 - install python(3.8)
 - install pip3
 - install pipenv
 - install celery
 - install postgres
 - install redis

## Testing and run:
```
// use requirements.txt
$ pip3 install -r requirements.txt

// use pipenv
$ pipenv install
$ pipenv shell

// run api
$ python3 app.py
or 
$ flask run

// create db migration
$ python3 manage.py db init
$ python3 manage.py db migrate

// run cron job
$ celery worker -A app.celery --loglevel=info --purge
$ celery beat -A app.celery --loglevel=info

// check schedule job in flower dashboard
$ flower -A app.celery --port=5555
open localhost:5555

// run test case
$ python3 src/test/main.test.py
```

## Docker:

- Dockerfile

build images and start container
```
docker build -t <username>/tropical-cyclone-api:<tag> .
docker run -p 5000:5000 -d <username>/tropical-cyclone-api:<tag>
docker exec -it <containerId> /bin/bash
docker logs <containerId>
```

check images and container
```
docker images
docker ps
docker ps -a
```

open localhost:5000

- docker-compose.yml

build images and start container
```
docker-compose build
docker-compose up
```

build images and start container in one line
```
docker-compose up -d --build
```

stop container
```
docker-compose stop
```

add tag to docker images
```
$ docker tag <imageId> <dockerHubUserName>/<imageName>:<tag>
```

push docker images to docker hub
```
$ docker push <dockerHubUserName>/<imageName>:<tag>
```

open localhost:5000