# Install Jenkins on Ubuntu

1. get aptitude key for Jenkins 
```
$ sudo wget -q -O - http://pkg.jenkins-ci.org/debian-stable/jenkins-ci.org.key |
sudo apt-key add -
```


2. add Jenkins binary source profile to apt source list
```
$ echo "deb http://pkg.jenkins-ci.org/debian-stable binary/" | sudo tee -a /etc/apt/sources.list 
```

3. install Jenkins

As Jenkins requires Java, we will install java and jenkins
```
$ sudo apt-get update && apt-get upgrade -y

$ sudo apt-get -y install openjdk-8-jdk

$ sudo apt-get -y install jenkins 
```


4. authenticate your jenkins credentials with password got from return value below
```
$ cat /var/lib/jenkins/secrets/initialAdminPassword
```
