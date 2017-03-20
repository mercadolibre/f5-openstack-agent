#!/bin/bash
docker build -t f5-openstack-agent:test .
docker rm f5-openstack-agent
/root/pipework —direct-phys br-mgmt $(docker run —hostname=f5_openstack_agent_DC4-D8-21vms -e METAL_HOST_ADDRESS=10.32.213.30 --restart=no --name f5-openstack-agent --net none -t -d f5-openstack-agent:test) 10.32.213.231/24@10.32.213.1
