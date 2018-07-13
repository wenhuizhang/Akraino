Here is a first pass at the heat template for serverless.  It will create three VMs and install kubernettes 1.9.x.  In the master (iot-k8s-1 by default) there is a setup_master.sh and setup_master.log that shows the results.  You can override any of the parameters by adding --parameter key=value to the heat create command, but below are the defaults.  Let me know if you have any issues.  I will have intermittent coverage for the next few days 404-372-0378.

David Plunkett

```

| parameters            | NetID: public-47                                                                                                                                |
|                       | k8_flavor: x1.large                                                                                                                             |
|                       | k8_image: ubuntu16_04                                                                                                                           |
|                       | k8_master: iot-k8s-1                                                                                                                            |
|                       | k8_minion1: iot-k8s-2                                                                                                                           |
|                       | k8_minion2: iot-k8s-3                                                                                                                           |
|                       | k8_network_cidr: 10.100.0.0/16                                                                                                                  |
|                       | k8_passwd: Serverless123                                                                                                                        |

```


`# ./run_openstack_cli.sh stack create -t ./serverless.yaml serverless-demo`

+---------------------+--------------------------------------------------------+
| Field               | Value                                                  |
+---------------------+--------------------------------------------------------+
| id                  | 641a1e6b-caff-440f-8be4-5d200d68fad3                   |
| stack_name          | serverless-demo                                        |
| description         | Hot Template to deploy a kubernetes cluster on Ubuntu. |
|                     |                                                        |
| creation_time       | 2018-07-05T17:15:42Z                                   |
| updated_time        | None                                                   |
| stack_status        | CREATE_IN_PROGRESS                                     |
| stack_status_reason | Stack CREATE started                                   |
+---------------------+--------------------------------------------------------+

`# ./run_openstack_cli.sh server list`

+--------------------------------------+-----------------------------------+--------+---------------------------------------------------------------+---------------------+
| ID                                   | Name                              | Status | Networks                                                      | Image Name          |
+--------------------------------------+-----------------------------------+--------+---------------------------------------------------------------+---------------------+
| 7a583323-942e-423f-9fb4-120ca06f5a8c | iot-k8s-1                         | ACTIVE | public-47=192.168.47.220                                      | ubuntu16_04         |
| ba693ae4-4297-4711-a41f-0045326b1e07 | iot-k8s-3                         | ACTIVE | public-47=192.168.47.211                                      | ubuntu16_04         |
| 5059c21f-f376-4a40-957b-264c7a4db752 | iot-k8s-2                         | ACTIVE | public-47=192.168.47.216                                      | ubuntu16_04         |
| 503250de-de44-4e9d-97d0-92699cb71485 | testvm-47                         | ACTIVE | public-47=192.168.47.218                                      | Cirros 0.3.5 64-bit |
| 17bce4d9-b9a6-49b3-bdfc-31d6bdec1d1a | testvm2                           | ACTIVE | public-onap-50=192.168.50.213                                 | Cirros 0.3.5 64-bit |
| 0d728bef-c3d5-457b-a819-ad632c45f3c0 | test-stack-01-server-aevfvhwxpduj | ACTIVE | test-stack-01-private_net-btftu43x3cv5=10.11.11.9, 172.24.4.5 | Cirros 0.3.5 64-bit |
+--------------------------------------+-----------------------------------+--------+---------------------------------------------------------------+---------------------+


`# ./run_openstack_cli.sh stack show serverless-demo`
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Value                                                                                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| id                    | 2505dfab-b743-4cc3-880f-e4b0a8e4ed2b                                                                                                            |
| stack_name            | serverless-demo                                                                                                                                 |
| description           | Hot Template to deploy a kubernetes cluster on Ubuntu.                                                                                          |
|                       |                                                                                                                                                 |
| creation_time         | 2018-07-05T17:41:18Z                                                                                                                            |
| updated_time          | None                                                                                                                                            |
| stack_status          | CREATE_COMPLETE                                                                                                                                 |
| stack_status_reason   | Stack CREATE completed successfully                                                                                                             |
| parameters            | NetID: public-47                                                                                                                                |
|                       | OS::project_id: 9550dd615d4f48dc90523558628363ea                                                                                                |
|                       | OS::stack_id: 2505dfab-b743-4cc3-880f-e4b0a8e4ed2b                                                                                              |
|                       | OS::stack_name: serverless-demo                                                                                                                 |
|                       | k8_flavor: x1.large                                                                                                                             |
|                       | k8_image: ubuntu16_04                                                                                                                           |
|                       | k8_master: iot-k8s-1                                                                                                                            |
|                       | k8_minion1: iot-k8s-2                                                                                                                           |
|                       | k8_minion2: iot-k8s-3                                                                                                                           |
|                       | k8_network_cidr: 10.100.0.0/16                                                                                                                  |
|                       | k8_passwd: Serverless123                                                                                                                        |
|                       |                                                                                                                                                 |
| outputs               | - description: This is the ip address of the Kubernetes master server.                                                                          |
|                       |   output_key: kube_master                                                                                                                       |
|                       |   output_value: 192.168.47.220                                                                                                                  |
|                       |                                                                                                                                                 |
| links                 | - href: http://heat.openstack.svc.cluster.local/v1/9550dd615d4f48dc90523558628363ea/stacks/serverless-demo/2505dfab-b743-4cc3-880f-e4b0a8e4ed2b |
|                       |   rel: self                                                                                                                                     |
|                       |                                                                                                                                                 |
| parent                | None                                                                                                                                            |
| disable_rollback      | True                                                                                                                                            |
| deletion_time         | None                                                                                                                                            |
| stack_user_project_id | 05591edd19074a68b5be29db5a569983                                                                                                                |
| capabilities          | []                                                                                                                                              |
| notification_topics   | []                                                                                                                                              |
| stack_owner           | None                                                                                                                                            |
| timeout_mins          | None                                                                                                                                            |
| tags                  | null                                                                                                                                            |
|                       | ...                                                                                                                                             |
|                       |                                                                                                                                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

`# ./run_openstack_cli.sh stack delete serverless-demo --yes`

