

# Kubenetes with Calico CNI

## 1. Install Kubenetes

#### 1.1 Verify NTP is Setup

Verify NTP is setup, if not install it.

```
# dpkg -l | grep "ntp" 
```
It should return: 
```
ii  ntp                                    1:4.2.8p4+dfsg-3ubuntu5.8                      amd64        Network Time Protocol daemon and utility programs
```

If not, install it through apt-get. 
```
# apt-get install -y ntp 
```


### 1.2 Add K8 Sources

```
# apt-get update 
# apt-get install -y apt-transport-https 
# curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - 
# echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" >/etc/apt/sources.list.d/kubernetes.list
# apt-get update 
```


### 1.3 Install Docker and K8

```
# apt-get install -y docker.io aufs-tools

# apt-get install -y kubeadm=1.11.0-00 kubelet=1.11.0-00 kubectl=1.10.2-00 kubernetes-cni=0.6.0-00 --allow-downgrades
```


### 1.4 Install Tools like Python
```
# apt-get install -y python2.7-dev python-pip python-setuptools python-crypto unzip 
# pip install --upgrade pip
```


### 1.5 Add hostname
```
$ export MYHOSTNAME=$(hostname)
$ export MYIP=$(ifconfig eno3 | grep -o " inet addr:[^ ]*" | cut -f 2 -d':')
$ echo -e "\n$MYHOSTNAME $MYIP\n" >> /etc/hosts
```
### 1.6 Verify K8 Installation
```
# kubelet --version
# kubeadm version
# kubectl --version
```
### 1.7 Start K8
```
# kubeadm reset
# kubeadm init
```

### 1.8 Cache clean
```
# apt-get clean
# hash -l
```


## 2. Install Calico


## 3. Build Cluster
