deploy:
	docker build -t f5-openstack-agent .
	docker tag -f f5-openstack-agent fury-registry.adminml.com/f5-openstack-agent
	docker push fury-registry.adminml.com/f5-openstack-agent

