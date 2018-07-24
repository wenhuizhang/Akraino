openstack image create --file ubuntu-16.04-server-cloudimg-amd64-disk1.img --disk-format qcow2 --container-format bare --public ubuntu16_04
export OS_AUTH_URL=http://keystone-api.openstack:35357/v3
export OS_IDENTITY_API_VERSION=3
export OS_INSECURE=1
export OS_USERNAME=admin
export OS_PASSWORD=password
export OS_PROJECT_DOMAIN_ID=default
export OS_PROJECT_NAME=admin
export OS_REGION_NAME=RegionOne
export OS_TENANT_NAME=admin
export OS_USER_DOMAIN_ID=default
 bash /opt/edgeboot/bin/create_pub_network.sh public 10.0.100.0/24 10.0.100.101 10.0.100.130 8.8.8.8 10.0.100.200
export OS_AUTH_URL=http://keystone-api.openstack.svc.cluster.local:35357/v3
export OS_IDENTITY_API_VERSION=3
export OS_INSECURE=1
export OS_USERNAME=admin
export OS_PASSWORD=password
export OS_PROJECT_DOMAIN_ID=default
export OS_PROJECT_NAME=admin
export OS_REGION_NAME=RegionOne
export OS_TENANT_NAME=admin
export OS_USER_DOMAIN_ID=default
