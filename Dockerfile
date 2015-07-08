FROM t4j/chainerapp-test:0.1

RUN pip install tornado

RUN mkdir -p /opt/t4j/serverapp
