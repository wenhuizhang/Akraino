
# Pcap Overview

## 0.Unzip

## 0.1 pcap.xz Format

Install xz-utils package first:

```
$ sudo apt-get install xz-utils
```

Use unxz command to extract .xz files:

```
$ unxz file.xz
```

Using with --decompress option of xz:

```
$ xz --decompress file.xz
```

## 1. Tcpdump 

### 1.1. Show packets in human readable way.

```
$ tcpdump -ttttnnr botnet-capture-20110810-neris.pcap

reading from file botnet-capture-20110810-neris.pcap, link-type EN10MB (Ethernet)
2011-08-10 05:01:40.475792 ARP, Request who-has 147.32.84.165 tell 147.32.84.1, length 46
2011-08-10 05:01:49.458501 ARP, Request who-has 147.32.84.165 tell 147.32.84.1, length 46
2011-08-10 05:02:30.575356 ARP, Request who-has 147.32.84.165 tell 147.32.84.1, length 46
2011-08-10 05:02:30.845058 ARP, Request who-has 147.32.84.165 tell 147.32.84.85, length 46
2011-08-10 05:02:31.844846 ARP, Request who-has 147.32.84.165 tell 147.32.84.85, length 46
2011-08-10 05:02:32.845480 ARP, Request who-has 147.32.84.165 tell 147.32.84.85, length 46
2011-08-10 05:02:33.562632 ARP, Request who-has 147.32.84.165 tell 147.32.84.1, length 46
...

```

### 1.2. Show packets in RAW format
```
$ tcpdump -qns 0 -A -r botnet-capture-20110810-neris.pcap

reading from file botnet-capture-20110810-neris.pcap, link-type EN10MB (Ethernet)
05:01:40.475792 ARP, Request who-has 147.32.84.165 tell 147.32.84.1, length 46
..........I.... T........ T...................
05:01:49.458501 ARP, Request who-has 147.32.84.165 tell 147.32.84.1, length 46
..........I.... T........ T...................
05:02:30.575356 ARP, Request who-has 147.32.84.165 tell 147.32.84.1, length 46
..........I.... T........ T...................
05:02:30.845058 ARP, Request who-has 147.32.84.165 tell 147.32.84.85, length 46
........TR..... TU....... T...................
05:02:31.844846 ARP, Request who-has 147.32.84.165 tell 147.32.84.85, length 46
........TR..... TU....... T...................
05:02:32.845480 ARP, Request who-has 147.32.84.165 tell 147.32.84.85, length 46
........TR..... TU....... T...................

```

### 1.3. Show pcakets in tcpick
```
$ tcpick -C -yP -r botnet-capture-20110810-neris.pcap

Starting tcpick 0.2.1 at 2018-07-30 15:32 UTC
Timeout for connections is 600
tcpick: reading from botnet-capture-20110810-neris.pcap
..)......... FDEBFCFFENEBEOCACACACACACACACAAA.. ..... ........... T.
..)......... FDEBFCFFENEBEOCACACACACACACACAAA.. ..... ........... T.
..)......... FDEBFCFFENEBEOCACACACACACACACAAA.. ..... ........... T.
..)......... FDEBFCFFENEBEOCACACACACACACACAAA.. ..... ........... T.
oL...........wpad.....
oL...........wpad.....
oL...........wpad............
..@.a.root-servers.net..nstld.verisign-grs.com.w............    :...Q.
............ FHFAEBEECOCACACACACACACACACACAAA.. ..
............ FHFAEBEECOCACACACACACACACACACAAA.. ..
..)......... FDEBFCFFENEBEOCACACACACACACACAAA.. ..... ........... T.
..)......... FDEBFCFFENEBEOCACACACACACACACAAA.. ..... ........... T.

```


