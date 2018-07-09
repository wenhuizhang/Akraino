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


## 2.Install Docker CE

2.1 Update the apt package index.
```
$ sudo apt-get update
```

2.2 Install the latest version of Docker CE, or go to the next step to install a specific version:
```
$ sudo apt-get install docker-ce
```
