# Install Suricata on Linux 

1. Install dependencies 

```
$ sudo apt-get install wget libnetfilter-queue-dev libnetfilter-queue1 libnfnetlink-dev pkg-config libmagic-dev build-essential libpcre3-dev libpcre3-dbg automake autoconf libtool libpcap-dev libnet1-dev libyaml-dev zlib1g-dev libcap-ng-dev libjansson-dev

$ sudo apt-get install apache2 

```
Add one line to ld:

`include /usr/local/lib`

to `/etc/ld.so.conf`

and then run `ldconfig`


2. Download the source 


```
$ wget https://www.openinfosecfoundation.org/download/suricata-4.0.4.tar.gz
$ tar -xvf suricata-4.0.4.tar.gz
```

3. Configure 

```
$ cd suricata-4.0.4
$ ./configure --sysconfdir=/etc --localstatedir=/var
```

4. Compile and Install

```
$ make
$ sudo make install
$ sudo make install-conf
$ sudo make install-rules
```

The configuration of rules is located at `/etc/suricata/rules ` . 

The binary of suricata is located at `/usr/bin/suricata`.


5. Configuration of IDS

Configuration file of IDS is located at ` /etc/suricata/suricata.yaml`. 

Disable eth's gro

```
$ sudo ethtool -K eth0 gro off lro off
```

Check modes available

```
$ sudo ldconfig
$ sudo /usr/local/bin/suricata --list-runmodes
```

Execute

```
$  docker run --privileged -v /home/wenhui/:/home -it wenhuizhang/suricata:v4
$ sudo /usr/local/bin/suricata -c /etc/suricata/suricata.yaml -i eth0 --init-errors-fatal
```

6. Check log files 

```
$ tail -f /var/log/suricata/fast.log

$ tail -f /var/log/suricata/eve.json
```

7. Check Deps

7.1 Check libraries in binary used for suricata in runtime. 

```

# ldd  /usr/local/bin/suricata
        linux-vdso.so.1 =>  (0x00007ffdb23ef000)
        libhtp.so.2 => /usr/local/lib/libhtp.so.2 (0x00007f3607893000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f360768b000)
        libmagic.so.1 => /usr/lib/x86_64-linux-gnu/libmagic.so.1 (0x00007f360746b000)
        libcap-ng.so.0 => /usr/lib/x86_64-linux-gnu/libcap-ng.so.0 (0x00007f3607266000)
        libpcap.so.0.8 => /usr/lib/x86_64-linux-gnu/libpcap.so.0.8 (0x00007f3607024000)
        libnet.so.1 => /usr/lib/x86_64-linux-gnu/libnet.so.1 (0x00007f3606e0b000)
        libjansson.so.4 => /usr/lib/x86_64-linux-gnu/libjansson.so.4 (0x00007f3606bfe000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f36069e1000)
        libyaml-0.so.2 => /usr/lib/x86_64-linux-gnu/libyaml-0.so.2 (0x00007f36067c2000)
        libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x00007f3606552000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f3606188000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f3605f6e000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f3607ab3000)

```

7.2 Check files accessed for suricata in runtime

```
$ mkdir out

$ cd out

# strace -ttff -o log /usr/local/bin/suricata -c /etc/suricata/suricata.yaml -i eth0 --init-errors-fatal

$ cat log.* > merge.txt

$ cat merge.txt | grep exec

$ cat merge.txt | grep clone

$ cat merge.txt | grep open
```




