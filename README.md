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
  $ ./dockerbin/1_build_serverapp-test.sh

####Start Container
  $ ./dockerbin/2_run_serverapp-test.sh

####Stop & Delete Container
  $ ./dockerbin/3_stop_serverapp-test.sh

####Login Container
  $ ./dockerbin/4_exec_serverapp-test.sh

####Start RestService
  $ docker exec -it serverapp-test-up service v-tornado start  

####Stop RestService
  $ docker exec -it serverapp-test-up service v-tornado stop  

####Start WebServer
  $ docker exec -it serverapp-test-up service v-nginx start

####Stop WebServer
  $ docker exec -it serverapp-test-up service v-nginx stop

####Debug Browser Access
  $ boot2docker ip
  192.168.59.103

ex. http://192.168.59.103:8080/  
ex. http://192.168.59.103:8888/

####Procedure Browser Access
- hosts setting

 ex. 192.168.59.103		mobilenurse.t4j.com
 ex. http://mobilenurse.t4j.com/form
