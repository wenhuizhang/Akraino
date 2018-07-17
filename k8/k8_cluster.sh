#!/bin/bash

# VERIFY NTP IS SETUP
if ! dpkg -l | grep "ntp " > /dev/nul; then apt-get install -y ntp 2>&1; fi

# ADD KUBERNETES SOURCES
apt-get update 2>&1
apt-get install -y apt-transport-https 2>&1
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  2>&1
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" >/etc/apt/sources.list.d/kubernetes.list
apt-get update 2>&1

# INSTALL DOCKER AND K8 IF THEY ARE NOT INSTALLED ALREADY.
#apt-get install -y docker.io aufs-tools  2>&1
apt-get install -y kubeadm=1.11.0-00 kubelet=1.11.0-00 kubectl=1.10.2-00 kubernetes-cni=0.6.0-00 --allow-downgrades  2>&1
# apt-get install -y kubelet=1.8.0-00 kubectl=1.8.0-00 kubernetes-cni --allow-downgrades  2>&1

# INSTALL PYTHON AND OTHER TOOLS
apt-get install -y python2.7-dev python-pip python-setuptools python-crypto unzip 2>&1
pip install --upgrade pip

# ADD HOSTNAME
MYHOSTNAME=$(hostname)
MYIP=$(ifconfig eno3 | grep -o " inet addr:[^ ]*" | cut -f 2 -d':')
echo -e "\n$MYHOSTNAME $MYIP\n" >> /etc/hosts

