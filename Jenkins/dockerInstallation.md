# Install Jenkins with Docker

1. check docker environment 
```
$ docker --version
```

2. pull jenkins docker image from web and verify 
```
$ docker images

$ docker pull jenkins/jenkins:lts

$ docker images
```

3. get Jenkins running on your system and expose through port 8080


```
$ docker run --detach --publish 8080:8080 --volume
jenkins_home:/var/jenkins_home --name jenkins jenkins/jenkins:lts
```


4. Open localhost:8080 in a browser and do authentication 
```
$ docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

```
