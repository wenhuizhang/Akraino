# Scalability Test 


## 1. Speed Testers 


### 1.1. tcpreplay
```
$ tcpreplay -i docker0 -tK --loop 5000  botnet-capture-20110810-neris.pcap
```

### 1.2 pkt-gen
```
$ root@pocnjrsv160:/home/wenhui/netmap/LINUX# ./build-apps/pkt-gen/pkt-gen -i docker0 -s 172.17.0.1  -d 172.17.0.1 -f tx -P ../../Akraino/Data/Pcap/botnet-capture-20110810-neris.pcap
```
