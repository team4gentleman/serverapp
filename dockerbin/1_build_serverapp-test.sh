#!/bin/bash
#
# docker build serverapp-test
#

if [ "$GIT_HOME" = "" ]; then
    echo "GIT_HOME must be set. exit."
    exit 1
fi

docker build --rm -t t4j/chainerapp-dummy:latest -f Dockerfiles/Dockerfile_chainerapp-dummy $GIT_HOME/serverapp/Dockerfiles

docker build --rm -t t4j/serverapp-test:latest -f Dockerfiles/Dockerfile_serverapp-test $GIT_HOME/serverapp/Dockerfiles

exit 0