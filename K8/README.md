

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
# kubectl version
```
### 1.7 Start K8
```
# kubeadm reset
# kubeadm init
```

### 1.8 Cache Clean
```
# apt-get clean
# hash -l
```


## 2. Install Calico

### 2.1 Initialize K8 Master
Init master and configure kubectl. 
```
# kubeadm reset
# kubeadm init --pod-network-cidr=192.168.0.0/16

# mkdir -p $HOME/.kube
# cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
# chown $(id -u):$(id -g) $HOME/.kube/config
```

### 2.2 Install Calico

Install Calico and a single node etcd.
```
# wget https://docs.projectcalico.org/v3.1/getting-started/kubernetes/installation/hosted/kubeadm/1.7/calico.yaml
# kubectl apply -f calico.yaml
```
### 2.3 Confirm 

Confirm that all of the pods are running. Use ***watch*** untill all pods is "Running".
```
# watch kubectl get pods --all-namespaces
```
The result is as following, uses ***CTRL + C*** to stop.
```
NAMESPACE    NAME                                       READY  STATUS   RESTARTS  AGE
kube-system  calico-etcd-x2482                          1/1    Running  0         2m
kube-system  calico-kube-controllers-6ff88bf6d4-tgtzb   1/1    Running  0         2m
kube-system  calico-node-24h85                          2/2    Running  0         2m
kube-system  etcd-jbaker-virtualbox                     1/1    Running  0         6m
kube-system  kube-apiserver-jbaker-virtualbox           1/1    Running  0         6m
kube-system  kube-controller-manager-jbaker-virtualbox  1/1    Running  0         6m
kube-system  kube-dns-545bc4bfd4-67qqp                  3/3    Running  0         5m
kube-system  kube-proxy-8fzp2                           1/1    Running  0         5m
kube-system  kube-scheduler-jbaker-virtualbox           1/1    Running  0         5m
```
### 2.4 Remove Taints 
Remove the taints on master node so that you can schedule pods on it.
```
# kubectl taint nodes --all node-role.kubernetes.io/master-
```
Confirm that you now have a node in your cluster.
```
# kubectl get nodes -o wide
```

## 3. Build Cluster
