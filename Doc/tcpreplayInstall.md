# Tcpreplay Installation

## 1. Installing and testing Netmap 

### 1.1. Download netmap from the official GitHub repository.

```
$ git clone https://github.com/luigirizzo/netmap.git
```

### 1.2 Configuration 

Enter the directory, Netmap is originally a BSD program, and in order to install on Linux we need to enter LINUX directory.
```
$ cd netmap/LINUX

# for all drivers
$ ./configure

# for normal drivers
$ ./configure --no-drivers

# to show supported drivers
$ ./configure --show-drivers
i40e  ixgbe  igb  e1000e  e1000  veth.c  forcedeth.c  virtio_net.c  r8169.c

# full list of help
$ ./configure --help
```

If kernel sources were prepared for out of tree compilation, additional parameters will be necessary:

```
$ ./configure --kernel-dir=/a/b/c/linux-A.B.C/
```

### 1.3. Compilation

Netmap comes with benchmark tools. 

Once netmap could be build and install by running:

```
$ make
$ make apps
$ sudo make install
```

### 1.4. Testing

#### 1.4.1 Load the netmap module.

```
$ modprobe netmap
```

If netmap enabled modules are used.
First unload the un-patched modules, and use veth module:

```
$ modprobe -r veth
$ modprobe netmap
$ modprobe veth_netmap
```
We can verify that modules are loaded with `lsmod`.

### 1.5 Testing 

Testing through ***pkt-gen*** application:
```
$ ./build-apps/pkt-gen -i eth0 -f tx -l 60
```

## 2. Install Tcpreplay




