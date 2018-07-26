# Installation of KVM

## 1. Install KVM
```
# apt-get install ubuntu-vm-builder
# apt-get install qemu-kvm qemu-system libvirt-bin bridge-utils
# apt-get install virt-manager python-spice-client-gtk

# systemctl enable --now libvirtd
# lsmod | grep kvm
# modprobe kvm_intel
# kvm-ok
```

## 2. Create Disk
```
#  qemu-img create -f raw test.img 10G
```

## 3. Download Image
```
# wget http://releases.ubuntu.com/16.04/ubuntu-16.04.4-server-amd64.iso
```

## 4. Execute
```
# virt-install --name test --hvm --ram 2048 --vcpu 1 --disk path=/home/wenhui/virsh/test.img,size=10 --network network:default --accelerate --vnc --vncport=5911 --cdrom ./ubuntu-16.04.4-server-amd64.iso -d
```
  
## 5. Test
```
# virt-viewer --connect qemu:///system --wait test
# virsh start test
```




