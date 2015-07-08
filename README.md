serverapp
=====================
## Requiements

- Docker (>=1.6)
- mac os?

## How to use

####Fork & Clone
- https://github.com/<GIT_ID>/chainer.git
- https://github.com/<GIT_ID>/serverapp.git
- https://github.com/<GIT_ID>/chainerapp.git
- https://github.com/<GIT_ID>/clientapp.git
-> ex. GIT_HOME=/Users/<OS_ID>/git

####Build DockerImage
  $ docker build -t t4j/chainerapp-test:0.1 /Users/<OS_ID>/git/chainerapp/.
  $ docker build -t t4j/serverapp-test:0.1 /Users/<OS_ID>/git/serverapp/.

####Start Container
docker run --name serverapp-test-up -i -t -d -p 8080:8080 ¥
  -v /Users/<OS_ID>/git/serverapp:/opt/t4j/serverapp ¥
  -v /Users/<OS_ID>/git/chainerapp:/opt/t4j/chainerapp ¥
  -v /Users/<OS_ID>/git/chainer:/opt/t4j/chainer ¥   t4j/serverapp-test:0.1

####Exec RestService
$ docker exec -it serverapp-test-up python /opt/t4j/serverapp/rest-service.py
-> stop[Ctrl+c]

####Login Container
$ docker exec -it serverapp-test-up bash

####Browser Access
$ boot2docker ip
192.168.59.103
-> http://192.168.59.103:8080/

####top & delete Container
$ docker stop serverapp-test-up
$ docker rm serverapp-test-up
