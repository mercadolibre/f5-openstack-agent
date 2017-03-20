FROM ubuntu:14.04

RUN apt-get update 
RUN apt-get update --fix-missing
RUN apt-get install -y python-pip 
RUN apt-get install -y python-dev 
RUN apt-get install -y build-essential 
RUN apt-get install -y libssl-dev 
RUN sudo apt-get install -y libffi-dev
RUN sudo apt-get install -y git


RUN pip install pytz==2015.7
RUN pip install eventlet==0.18.4
RUN pip install oslo.config==3.9.0
RUN pip install oslo.log==3.3.0
RUN pip install oslo.service==1.8.0
#RUN pip install git+git://github.com/openstack/neutron.git@8.1.1
RUN pip install git+https://github.com/openstack/neutron.git@8.1.1
RUN pip install cffi==1.5.2
RUN pip install git+git://github.com/openstack/neutron-lbaas.git@8.1.1
RUN pip install git+https://github.com/F5Networks/f5-openstack-lbaasv2-driver@mitaka

COPY . /app
WORKDIR /app
RUN pip install .

RUN chmod +x /app/confs/init_conf.sh

CMD ["/app/confs/init_conf.sh"]
