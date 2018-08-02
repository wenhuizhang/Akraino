#!/bin/bash

#function run


# set -n

run() {
    number=$1
    shift
    for i in `seq $number`; do
      $@
    done
}

export num=1
export file="result.txt"
export cmd1="/usr/local/bin/suricata -c /etc/suricata/suricata.yaml -r"
export cmd2=" ./botnet-capture-20110810-neris.pcap"
export cmd=$cmd1$cmd2

run $num $cmd

cat /var/log/suricata/stats.log | grep detect.alert
cat /var/log/suricata/stats.log | grep detect.alert | awk '{print $NF}' 
cat /var/log/suricata/stats.log | grep detect.alert | awk '{print $NF}' > $file
 