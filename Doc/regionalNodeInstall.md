# QuickStart Installation Guide for Regional Node

This guide instructs how to build and install an Akraino Edge Stack (AES) Regional Controller node.

The Regional Controller Node installation includes the following 3 components: (1) OS installation; (2) portal installation; (3) staging files on regional node. 

+ (1) OS Install
	1. Redfish Integrated Dell Remote Access Controller (iDRAC) bootstrapping and hardware configuration
	2. Linux OS (Ubuntu)

+ (2) Regional Controller
	1. PostgreSQL DB
	2. Camunda Workflow and Decision Engine
	3. Akraino Web Portal
	4. LDAP configuration 

+ (3) Supplementary Components
	1. Tempest 
	2. Yaml builds 
	3. ONAP
	4. Sample VNFs


This installation will walk you through the steps of installation of a `Bare metal server` through `Build server`.

```
This installation guide refers to the following by way of an example:
• 192.168.2.43 (aknode43): Build Server (Linux Server with a Docker Container)
• 192.168.2.42 (aknode42): Bare Metal Server
• 192.168.41.42: Bare Metal Server iDRAC
Steps herein presume the use of a root account. All steps are performed from the Build Server.
A clean, out-of-the-box Ubuntu environment is strongly recommended before proceeding.
```

#### To create a regional controller, it requires two servers:

1) Build server - any server or VM with Ubuntu installed;

2) Bare metal server - Dell server with no OS installed.


#### The Build Server, it has the following requirements:

• Any server or VM with Ubuntu Release 16.04

• Packages: Latest versions of sshpass, xorriso, and python-requests

• Docker 1.13.1 or later


#### The Bare Metal server has the following requirements:

• Dell PowerEdge R740 server with no installed OS

• Two interfaces for primary network connectivity bonding

• 802.1q VLAN tagging for primary network interfaces

#### The network requirements are:

1) The Build server must have connectivity to the Bare Metal server iDRAC interface;
	
2) The Build server must have connectivity to the Bare Metal server primary network;
	
3) If the Build server and the Bare Metal primary network are not on the same L2 network, 
then a DHCP relay/helper must be setup to forward DHCP requests from the Bare Metal 
primary network interface to the Build server.



This installation guide uses Node 42 and Node 44 as an example, to walk you through steps of installation. 
```
Node 42 is a Bare Metal Server. 
Node 44 is a Linux Server with Container.
```


## 1. System Check 

On ***Build Server*** 

### 1.1 Check OS and Docker version on Linux Server

Ensure Ubuntu Release 16.04 (specifically) and Docker 1.13.1 (or later) are installed:

```
# lsb_release -rs
16.04
# docker --version
Docker version 1.13.1, build 092cba3
```


### 1.2 Check the Packages

Ensure Python 2, specifically version 2.7.12 or later is installed. Ensure the latest versions of sshpass, xorriso, and python-requests are installed.

```
# python --version
Python 2.7.12

# apt install --upgrade sshpass xorriso python-requests
Reading package lists... Done
Building dependency tree
Reading state information... Done
python-requests is already the newest version (2.9.1-3).
sshpass is already the newest version (1.05-1).
xorriso is already the newest version (1.4.2-4ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 107 not upgraded
```

### 1.3 Check Network Setup

1) The Build Server must have connectivity to the Bare Metal Server iDRAC interface on ports 22 (ssh) and 5900 (vnc).;
	
2) The Bare Metal Server must be reachable from the Build Server;
	
3) The Build Server and Bare Metal Server primary networks must have one of the following characteristics::

• The networks must be located on the same L2 network, or

• DHCP requests must be forwarded from the Bare Metal Server primary network interface to the Build Server (e.g., via a DHCP relay/helper).



Specific steps to achieve this connectivity are beyond the scope of this guide. However, some verification can be performed.

1. Verify that at least ports 22 and 5900 are open on the Bare Metal Server iDRAC interface:

```
# nmap -sS 192.168.41.42
Starting Nmap 7.01 ( https://nmap.org ) at 2018-07-10 13:55 UTC
Nmap scan report for 192.168.41.42
Host is up (0.00085s latency).
Not shown: 996 closed ports
PORT STATE SERVICE
22/tcp open ssh
80/tcp open http
443/tcp open https
5900/tcp open vnc
Nmap done: 1 IP address (1 host up) scanned in 1.77 seconds
```

2. Use nmap to check for a "clean slate" Bare Metal Server. The results will show the host as being down (due to no OS).

```
# nmap -sS 192.168.2.42
Starting Nmap 7.01 ( https://nmap.org ) at 2018-07-10 13:55 UTC
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 0.63 seconds
```
Verification of the Build Server and Bare Metal Server primary networks is beyond the scope of this guide.


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

Clone the Redfish Bootstrapping Scripts as part of Akraino tools. 

```
$ git clone https://gerrit.akraino.org/r/redfish /opt/akraino/tools
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
Beginning /opt/akraino/tools/install_server_os.sh as user [root] 
in pwd [/opt/akraino/server-config] with home [/root]
Tools are ready in [/opt/akraino]
WARNING:  Preparing to build server [aknode44] using oob ip [192.168.41.42].  
Beginning in 10 seconds ..........
Beginning bare metal install of os at Mon Jul 2 18:57:32 UTC 2018

...

Processing triggers for libc-bin (2.23-0ubuntu10) ...
SUCCESS:  Completed bare metal install of regional server [aknode44] at Mon Jul 2 20:09:35 UTC 2018
SUCCESS:  Try connecting with 'ssh root@192.168.2.42' as user root
Elapsed time was 9 minutes and 22 seconds
```


### 4.4 Get region code on iDRAC

Clone scripts to build your region node to your workspace. 

```
$ git clone https://gerrit.akraino.org/r/regional_controller /opt/akraino/region
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



