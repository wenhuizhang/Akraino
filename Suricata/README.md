# Install Suricata on Linux 

1. Install dependencies 

```
$ sudo apt-get install wget libnetfilter-queue-dev libnetfilter-queue1 libnfnetlink-dev pkg-config libmagic-dev build-essential libpcre3-dev libpcre3-dbg automake autoconf libtool libpcap-dev libnet1-dev libyaml-dev zlib1g-dev libcap-ng-dev libjansson-dev

$ sudo apt-get install apache2 php5 mysql-server php5-mysql

```


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
$ sudo /usr/local/bin/suricata --list-runmodes
```

Execute

```
$ sudo /usr/local/bin/suricata -c /etc/suricata/suricata.yaml -i eth0 --init-errors-fatal
```

6. Check log files 

```
$ tail -f /var/log/suricata/fast.log

$ tail -f /var/log/suricata/eve.json
```

7. Check Deps

Check libraries in binary used for suricata in runtime. 

```
$ mkdir out

$ cd out

# strace -ttff -o log /usr/local/bin/suricata -c /etc/suricata/suricata.yaml -i eth0 --init-errors-fatal

$ grep ./ exec

$ grep ./ fork
```




