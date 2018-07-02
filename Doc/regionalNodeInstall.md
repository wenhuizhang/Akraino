# QuickStart Installation Guide for Regional Node

This guide helps you build and install Regional Node of Akraino Stack.

There are 9 components involved in this installation of regional node. 

1) Redfish OS

2) Camunda Workflow and Decision Engine

3) PostgressDB

4) LDAP configuration

It also downloads portal files:

5) Tempest 

6) Yaml builds 

7) ONAP

8) Sample VNFs 

9) Airship in a bottle tar file


This installation will walk you through the steps of installation of a `Bare metal server` through `Build server`.

#### To create a regional controller requires two servers:

1)	Build server - any server or VM with Ubuntu installed;

2)	Bare metal server - Dell server with no OS installed.


#### The Build Server has the following requirements:

1) Ubuntu 16.04.1;

2) Docker version 1.13.1;

3) Packages of sshpass, xorriso and python-requests. 


#### The Bare Metal server  has the following requirements:

1) Dell PowerEdge R740 server;
	
2) Two interfaces to bond for the primary network connectivity;

3) 802.1q vlan tagging on primary network interfaces.

#### The network requirements are:

1)	The Build server must have connectivity to the Bare Metal server iDRAC interface;
	
2) The Build server must have connectivity to the Bare Metal server primary network;
	
3) If the Build server and the Bare Metal primary network are not on the same L2 network, 
then a DHCP relay/helper must be setup to forward DHCP requests from the Bare Metal 
primary network interface to the Build server.



This installation uses Node 42 and Node 44 as an example for walking through steps of installation. 
```
Node 42 is a Bare Metal Server. 
Node 44 is a Linux Server with Container.
```


## 1. Check System 


### 1.1 Check OS version on Linux Server

Check what OS is on Linux Server, a `Ubuntu 16.04.1` is required.
```
$ uname -rsv
Linux 4.13.0-45-generic #50~16.04.1-Ubuntu SMP Wed May 30 11:18:27 UTC 2018

```

### 1.2 Check Docker version on Linux Server

Check what Docker version it is, a version of 1.13.1 or higher is required. 

```
$ docker --version
Docker version 1.13.1, build 092cba3
```

### 1.3 Check the Packages

Check what versions are there for packages of sshpass, xorriso and python-requests. 
We are requiring python version of 2.7.12. 

```
$ sudo apt install sshpass xorriso python-requests

Reading package lists... Done
Building dependency tree
Reading state information... Done
python-requests is already the newest version (2.9.1-3).
sshpass is already the newest version (1.05-1).
xorriso is already the newest version (1.4.2-4ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 107 not upgraded.
```

### 1.4 Check Network Setup

1)	The Build server must have connectivity to the Bare Metal server iDRAC interface;
	
2) The Build server must have connectivity to the Bare Metal server primary network;
	
3) If the Build server and the Bare Metal primary network are not on the same L2 network, 
then a DHCP relay/helper must be setup to forward DHCP requests from the Bare Metal 
primary network interface to the Build server.



## 2. Setup Environment

By default, Akarino Tools will be built under folder `/opt/`.

Please make sure that you have a clean environment for the installation. 

### 2.1 Create a folder for base installation of Akraino.

```
$ mkdir /opt/akraino
$ cd /opt/akraino
```

### 2.2 Setup environment variables

Create your environment variable file.

```
$ vim .akrainorc
```

A sample `.akrainorc` file is as below:

```
# /opt/akraino/.akrainorc: executed by bash(1) for env of akraino setup.

export TARGET_SERVER_IP=192.168.2.42
export DB_SCHEMA_VERSION=1.0.0-201806260417
export CAMUNDA_WORKFLOW_VERSION=1.0.0
export PORTAL_VERSION=5.0
export TEMPEST_VERSION=0.0.1-SNAPSHOT
export ONAP_VERSION=0.0.1-SNAPSHOT
export YAML_BUILD_VERSION=0.0.1-SNAPSHOT
export SAMPLE_VNF_VERSION=0.0.1-SNAPSHOT
```

Source your setup in a shell. 

```
$ source /opt/akraino/.akrainorc
```


## 3. Setup Repositories

### 3.1 Setup repository of Akraino tools

Clone the Redfish OS as part of Akraino tools. 

```
$ git clone http://gerrit.att-akraino.org/redfish.git /opt/akraino/tools
```

## 4. Configure and Compile

### 4.1 Create server configuration

In this step, you will create a server configuration from a template. 

The template is stored in `/opt/akraino/server-config`. 

In the steps below, please change **aknode42rc** ( `/opt/akraino/server-config/aknode42rc` )
into the `bare metal server name` you are setting up with. 

```
$ mkdir -p /opt/akraino/server-config
$ cp /opt/akraino/tools/serverrc.template /opt/akraino/server-config/aknode42rc
```

### 4.2 Update configuration for your server 

Update configuration files for your target bare metal server.
```
$ vi /opt/akraino/server-config/aknode42rc

```
A sample configuration file is as below, please update the password and ips etc. etc. 

```
# Set the ip and port to use when creating the web server
BUILD_WEBIP=192.168.2.5
BUILD_WEBPORT=8090

# host name for server
SRV_NAME=aknode42

# server oem - Dell or HPE (case sensitive)
SRV_OEM=Dell

# out of band interface information for server (idrac/ilo/etc)
SRV_OOB_IP=192.168.41.42
SRV_OOB_USR=root
SRV_OOB_PWD=calvin

# mac address of server to be used during the build - not required for Dell servers
# SRV_MAC=3c:fd:fe:b8:10:60

# name of network interface used during build when ipxe.efi is booted and when os is booted
# ipxe numbers ports from 0-n in pci bus order.
# the netx value will depend on how many nics are in the server
# and which pci device number is assigned to the slot
SRV_IPXE_INF=net4

# the build interface is the nic used by the Ubuntu installed to load the OS
SRV_BLD_INF=enp94s0f0

# the boot device is the device name on which the OS will be loaded
SRV_BOOT_DEVICE=sdg

# ipxe script to use - based on the os version and kernel to install
# valid options are script-hwe-16.04.4-amd64.ipxe or script-16.04.4-amd64.ipxe
SRV_BLD_SCRIPT=script-hwe-16.04.4-amd64.ipxe

# template xml file to set bios and raid configuration settings
SRV_BIOS_TEMPLATE=dell_r740_g14_uefi_base.xml.template
SRV_BOOT_TEMPLATE=dell_r740_g14_uefi_httpboot.xml.template
SRV_HTTP_BOOT_DEV=NIC.Slot.3-1-1

# VLAN to use during build and for final network configuration
SRV_VLAN=41

# basic network information for dhcp config and final server network settings
SRV_MTU=9000
SRV_IP=192.168.2.42
SRV_SUBNET=192.168.2.0
SRV_NETMASK=255.255.255.0
SRV_GATEWAY=192.168.2.200
SRV_DNS=192.168.2.85
SRV_DOMAIN=lab.akraino.org
SRV_DNSSEARCH=lab.akraino.org
SRV_NTP=ntp.ubuntu.org

# root password for server being built
SRV_PWD=akraino,d

# network bond information
SRV_BOND=bond0
SRV_SLAVE1=enp94s0f0
SRV_SLAVE2=enp94s0f1
```


### 4.3 Run and Install 

Run and install scripts you write in step 4.2 . 

```
$ /opt/akraino/tools/install_server_os.sh --rc /opt/akraino/server-config/aknode42rc --no-confirm
```

It will take quite a while, relax and get a cup of coffee/tea :-P 

If you see something as below, you are good to go.

```
$ /opt/akraino/tools/install_server_os.sh --rc /opt/akraino/server-config/aknode42rc --no-confirm
Beginning /opt/akraino/tools/install_server_os.sh as user [root] in pwd [/opt/akraino] with home [/root]
Tools are ready in [/opt/akraino]
WARNING:  Preparing to build server [aknode42] using oob ip [192.168.41.42].  Beginning in 10 seconds ..........
Beginning bare metal install of os at Fri Jun 29 23:12:26 UTC 2018

...

SUCCESS:  Completed bare metal install of regional server [aknode42] at ...
SUCCESS:  Try connecting with 'ssh root@192.168.2.42' as user root
Elapsed time was 10 minutes and 31 seconds
```


### 4.4 Get region code on iDRAC

Clone scripts to build your region node to your workspace. 

```
$ git clone http://gerrit.att-akraino.org/regional_controller.git /opt/akraino/region
```

Then copy portal build scripts to iDRAC. 

```
$ scp /opt/akraino/region/start_akraino_portal.sh root@$TARGET_SERVER_IP:/tmp/
```

### 4.5 Build your server node

Then logon to your iDRAC and start deploying. 


```
$ ssh root@$TARGET_SERVER_IP "bash /tmp/start_akraino_portal.sh \
$DB_SCHEMA_VERSION $CAMUNDA_WORKFLOW_VERSION $PORTAL_VERSION"
```

Again, it will take quite a while, relax and get a cup of coffee/tea :-P 

If you see something as below, you are good to go.

```
...

Setting up tempest repository
Setting up yaml builds repository
Setting up ONAP repository
Setting up sample vnf repository
SUCCESS:  Portal install completed
```



