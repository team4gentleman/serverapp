serverapp
=====================
## Requiements

- Docker (>=1.6)
- mac os?

## How to use

####Fork & Clone
- https://github.com/(GIT_ID)/chainer.git
- https://github.com/(GIT_ID)/serverapp.git
- https://github.com/(GIT_ID)/chainerapp.git
- https://github.com/(GIT_ID)/clientapp.git

####First Setting
ex.
vi ~/.bash_profile
exportGIT_HOME=/Users/(OS_ID)/git

####Build DockerImage
  $ ./1_build_serverapp-test.sh

####Start Container
  $ ./2_run_serverapp-test.sh

####Stop & Delete Container
  $ ./3_stop_serverapp-test.sh

####Login Container
  $ ./4_exec_serverapp-test.sh

####Exec RestService
  $ docker exec -it serverapp-test-up python /opt/t4j/serverapp/rest-service.py

stop[Ctrl+c]

####Browser Access
  $ boot2docker ip
  192.168.59.103

ex. http://192.168.59.103:8080/
