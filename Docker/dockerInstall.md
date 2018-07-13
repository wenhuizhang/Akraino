



# Install Docker

We are installing using the repository for Docker CE. 

## 1. Set Environment 

1.1 Update the apt package index:

```
$ sudo apt-get update
```

1.2 Install packages to allow apt to use a repository over HTTPS:

```
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
 ```     

1.3 If there is umet dependencies , use
```
$ sudo apt-get install -f
```


1.4 Add Docker’s official GPG key:
```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
Download and import Docker’s public key for CS packages:
```
$ curl -fsSL 'https://sks-keyservers.net/pks/lookup?op=get&search=0xee6d536cf7dc86e2d7d56f59a178ac6c6238f52e' | sudo apt-key add -
``` 
1.5 Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.
```
$ sudo apt-key fingerprint 0EBFCD88
```


1.6 The `lsb_release -cs` sub-command below returns the name of your Ubuntu distribution, such as xenial.

```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

```
$ sudo add-apt-repository \
   "deb https://packages.docker.com/1.13/apt/repo/ \
   ubuntu-$(lsb_release -cs) \
   main"
```   
   
## 2.Install Docker CE

2.1 Update the apt package index.
```
$ sudo apt-get update
$ sudo apt-cache madison docker-engine
```

2.2 Install the latest version of Docker CE, or go to the next step to install a specific version:
```
$ sudo apt-get install docker-ce=<version>
```

## 3. Confirm 

3.1 Confirm the Docker daemon is running

```
$ sudo docker info
```
3.2 Add non-sudo access to the Docker socket by adding your user to the docker group.

```
$ sudo usermod -a -G docker $USER
```
Log out and log back in to have your new permissions take effect.
