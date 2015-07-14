serverapp
=====================
## Requiements

- Docker (>=1.6)
- mac os?

## How to use

####Fork & Clone
- https://github.com/(GIT_ID)/serverapp.git
- https://github.com/(GIT_ID)/chainerapp.git

####First Setting
ex.
vi ~/.bash_profile
exportGIT_HOME=/Users/(UID)/git

####Build DockerImage
  $ ./1_build_serverapp-test.sh

####Start Container
  $ ./2_run_serverapp-test.sh

####Stop & Delete Container
  $ ./3_stop_serverapp-test.sh

####Login Container
  $ ./4_exec_serverapp-test.sh

####Start RestService
  $ docker exec -it serverapp-test-up service v-tornado start  
  $ docker exec -it serverapp-test-up service w-tornado start

####Stop RestService
  $ docker exec -it serverapp-test-up service v-tornado stop  
  $ docker exec -it serverapp-test-up service w-tornado stop

####Start WebServer
  $ docker exec -it serverapp-test-up service v-nginx start

####Stop WebServer
  $ docker exec -it serverapp-test-up service v-nginx stop

####Browser Access
  $ boot2docker ip
  192.168.59.103

ex. http://192.168.59.103:8080/  
ex. http://192.168.59.103:8888/
