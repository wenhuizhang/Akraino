
# Install VM (KVM)

## 1. Install KVM
```
$ sudo apt install qemu-kvm libvirt-bin virtinst bridge-utils cpu-checker
$ kvm-ok
## configure bridged networking as described here
$ sudo vi /etc/network/interfaces
$ sudo systemctl restart networking
$ sudo brctl show
```

## 2. Install uvtool
```
$ sudo apt install uvtool
```

## 3. Download the Ubuntu Image 

Download Ubuntu Cloud image for KVM through ` uvt-simplestreams-libvirt`.

Update/grab Ubuntu 16.04 LTS (xenial/amd64) image run:

```
$ uvt-simplestreams-libvirt --verbose sync release=xenial arch=amd64
```
To update uvtool’s libvirt volume storage pool with all current amd64 images, run:

```
$ uvt-simplestreams-libvirt sync arch=amd64
```

Grab development version:
```
$ uvt-simplestreams-libvirt --verbose sync --source http://cloud-images.ubuntu.com/daily release=bionic arch=amd64
```

## 4. Check Local Images

Pass the query option to queries the local mirror:
```
$ uvt-simplestreams-libvirt query 
```

## 5. Optional: Create the SSH keys

If you do not have keys, just use:

```
$ ssh-keygen
```

## 6. Create VMs

Create the VM named vm1:
```
$ uvt-kvm create test release=xenial
```
By default vm1 created using the following characteristics:
```
    RAM/memory : 512M
    Disk size: 8GiB
    CPU: 1 vCPU core
```

Specify Ubuntu release and arch:

```
$ uvt-kvm create test release=xenial arch=amd64 \
--memory 10240 \
--cpu 1 \
--disk 40 \
--ssh-public-key-file ~/.ssh/id_rsa.pub
```

To control ram, disk, cpu, and other characteristics use the following syntax:

```
$ uvt-kvm create vm1 \
--memory MEMORY \
--cpu CPU \
--disk DISK \
--bridge BRIDGE \
--ssh-public-key-file /path/to/your/SSH_PUBLIC_KEY_FILE \
--packages PACKAGES1, PACKAGES2, .. \
--run-script-once RUN_SCRIPT_ONCE \
--password PASSWORD
```


## 7. Log In

Login to the vm named vm1.

```
$ uvt-kvm ssh vm1
```

Use the regular ssh command client:

```
$ ssh ubuntu@192.168.122.52
$ ssh -i ~/.ssh/id_rsa ubuntu@192.168.122.52
```

## 8. Debug

To get help, run:

```
$ uvt-kvm -h
$ uvt-kvm create -h
```
To find out the IP address of the vm1, run:

```
$ uvt-kvm ip vm1
```

To list all VMs run

```
$ uvt-kvm list
```

Once vim created you can use the virsh command as usual:

```
$ virsh list
```

## 9.Delete VM

To destroy/delete your VM named vm1, run:

```
$ uvt-kvm destroy vm1
```

To find out the IP address of the vm1, run:

```
$ uvt-kvm ip vm1
```

### P.S. Network Issues

When meet some network issues, pn the iDRAC
```
> console com2
```
And check if routing is working fine.

```
root@pocnjrsv160:/home/wenhui# netstat -rn
root@pocnjrsv160:/home/wenhui# route add -net default gw 135.25.28.50
root@pocnjrsv160:/home/wenhui# route delete -net default gw 192.168.0.1
```
