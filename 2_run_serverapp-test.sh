#!/bin/bash
#
# docker run serverapp-test
#
docker run --name serverapp-test-up -i -t -d -p 8080:8080 \
  -v $GIT_HOME/serverapp:/opt/t4j/serverapp \
  t4j/serverapp-test:latest
