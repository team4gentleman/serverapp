GIT_HOME=/Users/naoki/git

docker run --name serverapp-test-up -i -t -d -p 8080:8080 \
  -v $GIT_HOME/serverapp:/opt/t4j/serverapp \
  -v $GIT_HOME/chainerapp:/opt/t4j/chainerapp \
  -v $GIT_HOME/chainer:/opt/t4j/chainer \
  t4j/serverapp-test:latest
