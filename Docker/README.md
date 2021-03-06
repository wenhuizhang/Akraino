

# Docker Commands 

## 1. Boot a docker

1.1 Execute docker images and attach it to a network interface. 

```
# docker run -it --net=host --name=suricata docker/docker-image -i <interface>
```

1.2 Execute docker images and attach it to a network interface, and get a log file. 

Then you could check Suricata logs from outside the container.

```
# docker run -it --net=host -v $(pwd)/logs:/var/log/suricata docker/docker-image -i <interface>
```


## 2. Start a second container with volumes-from:


Expose `/var/log/suricata` from the Suricata container as `/var/log/suricata` in the Logstash container.

```
# docker run -it --net=host --volumes-from=suricata logstash /bin/bash


```



## 3. Stop a docker

Sometimes you need to stop k8.

```
# kubeadm reset
```

3.1 stop all containers

```
# docker kill $(docker ps -q)
```

3.2 remove all containers

```
# docker rm $(docker ps -a -q)
```

3.3 remove all docker images

```
# docker rmi $(docker images -q)
```

3.4 remove all docker volumes

```
# docker volume ls -qf dangling=true | xargs -r docker volume rm
```

## 4. Images

In the case of aufs:

`/var/lib/docker/aufs/diff/<id>` has the file contents of the images.

`/var/lib/docker/repositories-aufs` is a JSON file containing local image information. 

This can be viewed with the command docker images.

## 5. Build Images:
```
$ docker build -t wenhuizhang/suricata:v3  .

$ docker run -it --rm wenhuizhang/suricata:v3 bash
```

## 6. Push Images 
```
$ docker login --username=wenhuizhang --email=wenhui@gwmail.gwu.edu
$ docker commit c0d0a207c93e wenhuizhang/suricata:v3
$ docker push wenhuizhang/suricata
```

## 7. Push to Bob
```
$ docker build -f docker/Dockerfile -t edgeboot:latest .
$ docker tag edgeboot:latest edgeboot:$(VERSION)
            
$ docker tag edgeboot:latest mtmac5.research.att.com/edgeboot:$(VERSION)
$ docker push mtmac5.research.att.com/edgeboot:$(VERSION)
```

## 8. Docker Copy
```
$  docker cp suricata-4.0.4.tar.gz pensive_dubinsky:/root/
$  docker cp emerging.rules.tar.gz pensive_dubinsky:/root/

```
