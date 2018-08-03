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

#### 1.4.1. Load the netmap module.

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

#### 1.4.2. Verify netmap module.

We can verify that modules are loaded with `lsmod`.

### 1.5. Testing 

Testing through ***pkt-gen*** application:

```
$ ./build-apps/pkt-gen -i eth0 -f tx -l 60
```

## 2. Install Tcpreplay

### 2.1. Dependencies

```
# Ubuntu or Debian systmes:
sudo apt-get install build-essential libpcap-dev
```

### 2.2. Basic Compilation and Installation

Extract tarball ***tcpreplay-4.2.5.tar***, change to root directory, then do:

```
$ tar -xf tcpreplay-4.2.5.tar
$ cd tcpreplay-4.2.5
$ ./configure
$ make
$ sudo make install
```
Optionally you can run the tests to ensure that your installation is fully functional:

```
$ sudo make test
```

### 2.3. Netmap Compilation and Installation

For Linux, download latest and install netmap from `http://info.iet.unipi.it/~luigi/netmap/` .

Extracted netmap into `/usr/src/` or `/usr/local/src` to avoid extra configure options. 

Otherwise, specify the netmap source directory, for example:

```
$ ./configure --with-netmap=/home/fklassen/git/netmap
$ make
$ sudo make install
```

### 2.4. Other configurations

Some of the more interesting ones are:
```
–enable-debug – useful for debugging bugs and crashes.
–enable-64bits – use 64 bit counters to handle large pcap files & looping
–enable-libnet – link to libnet. Note that libnet support has been deprecated due to various bugs which have not been fixed in over a year.
–with-libnet – specify root path to libnet (something like –with-libnet=/usr/local)
–with-libpcap – specify root path to libpcap
–with-netmap – specify root path to netmap
–with-tcpdump – specify path to tcpdump executable
–enable-tcpreplay-edit – compile tcpreplay with packet editing support
You can also manually select a particular method to inject packets:
–enable-force-pf – force tcpreplay to use Linux’s PF_PACKET to send packets
–enable-force-bpf – force tcpreplay to use Free/Net?/OpenBSD or OS X’s BPF interface to send packets
–enable-force-libnet – force tcpreplay to use Libnet to send packets
–enable-force-inject – force tcpreplay to use Libpcap’s pcap_inject() API to send packets
–enable-force-sendpacket – force tcpreplay to use Libpcap’s pcap_sendpacket() API to send packets
If you’re having compatibility issues with a system-installed GNU Autogen, you may want to consider these options:
–disable-local-libopts – Don’t use the libopts tearoff supplied with tcpreplay (default is enabled)
–disable-libopts-install – don’t install the libopts library files
```





