FROM ubuntu:14.04

RUN apt-get update 
RUN apt-get update --fix-missing
RUN  apt-get install -y python-pip 
RUN  apt-get install -y python-dev 
RUN  apt-get install -y build-essential 
RUN sudo apt-get install -y libffi-dev
COPY . /app

WORKDIR /app

RUN pip install eventlet
RUN pip install oslo.config
RUN pip install oslo.log   
RUN pip install oslo.service



RUN pip install .

RUN chmod +x /app/confs/init_conf.sh

CMD ["/app/confs/init_conf.sh"]
