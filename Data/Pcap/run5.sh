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

export num=500
export cmd="/usr/local/bin/suricata -c /etc/suricata/suricata.yaml -r ./out.pcap5"

run $num $cmd

cat /var/log/suricata/stats.log | grep detect.alert
cat /var/log/suricata/stats.log | grep detect.alert | awk '{print $NF}' 
cat /var/log/suricata/stats.log | grep detect.alert | awk '{print $NF}' > result5.txt
 
