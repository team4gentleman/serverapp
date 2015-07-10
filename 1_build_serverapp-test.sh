#!/bin/bash
#
# docker build serverapp-test
#
cp Dockerfile_chainerapp-dummy Dockerfile
docker build -t t4j/chainerapp-dummy:latest .

cp Dockerfile_serverapp-test Dockerfile
docker build -t t4j/serverapp-test:latest .

rm -f Dockerfile
