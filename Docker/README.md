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
