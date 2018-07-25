# Installation of Qemu

 virt-install --name test --hvm --ram 2048 --vcpu 1 --disk path=/home/wenhui/virsh/test.img,size=10 --network network:default --accelerate --vnc --vncport=5911 --cdrom ./ubuntu-16.04.4-server-amd64.iso -d
 
 
   564  lsmod | grep kvm
  565  modprobe kvm_intel
  566  lsmod | grep kvm
  567  systemctl enable --now libvirtd
  568  apt-get install ubuntu-vm-builder
  569  apt-get install qemu-kvm qemu-system libvirt-bin bridge-utils
  570  apt-get install virt-manager python-spice-client-gtk
  571  kvm-ok
  572  lsmod | grep kvm
  
  
  qemu-img create -f raw test.img 10G
  
  
wget http://releases.ubuntu.com/16.04/ubuntu-16.04.4-server-amd64.iso

  
  
  627  virt-viewer --connect qemu:///system --wait test
  628  virsh start test



