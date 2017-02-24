#!/bin/bash
#echo "icontrol_hostname = 10.49.1.11,10.49.1.12"  >> /app/confs/f5-openstack-agent.ini
#echo "icontrol_username = ktest" >> /app/confs/f5-openstack-agent.ini
#echo "icontrol_password = B0n3l355" >> /app/confs/f5-openstack-agent.ini

f5-oslbaasv2-agent --config-file /opt/f5-openstack-agent/confs/f5-openstack-agent.ini --config-file /opt/f5-openstack-agent/confs/neutron.conf --config-file /opt/f5-openstack-agent/confs/ml2_conf.ini
