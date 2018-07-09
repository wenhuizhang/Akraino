# Install Ubuntu 

## 1. Obtaining Source

```
$ git clone git://kernel.ubuntu.com/ubuntu/ubuntu-<release codename>.git
```

## 2. Build Environment

```
$ sudo apt-get build-dep linux-image-$(uname -r)
```


## 3. Modifying Configuration

This step can be skipped if no configuration changes are wanted. 
```
$ chmod a+x debian/rules
$ chmod a+x debian/scripts/*
$ chmod a+x debian/scripts/misc/*
$ fakeroot debian/rules clean
$ fakeroot debian/rules editconfigs 

```

## 4. Building Kernel

```
$ fakeroot debian/rules clean

# quicker build:
$ fakeroot debian/rules binary-headers binary-generic binary-perarch

# if you need linux-tools or lowlatency kernel, run instead:
$ fakeroot debian/rules binary

```

## 5. Insatall Ubuntu

```
$ cd ..
$ ls *.deb
    linux-headers-4.13.0-45_4.13.0-45.50~16.04.1_all.deb
    linux-headers-4.13.0-45-generic_4.13.0-45.50~16.04.1_amd64.deb
    linux-cloud-tools-4.13.0-45-generic_4.13.0-45.50~16.04.1_amd64.deb
    linux-image-4.13.0-45-generic_4.13.0-45.50~16.04.1_amd64.deb
    linux-image-extra-4.13.0-45-generic_4.13.0-45.50~16.04.1_amd64.deb
    linux-tools-4.13.0-45-generic_4.13.0-45.50~16.04.1_amd64.deb
$ sudo dpkg -i *.deb
```

## 6. Debugging

Mayebe you will have to get header files ready before you compile. 


Maybe you will have to download 2 images below as well, or build them from scratch. 

```
linux-hwe-cloud-tools-4.13.0-45_4.13.0-45.50~16.04.1_amd64.deb
inux-hwe-tools-4.13.0-45_4.13.0-45.50~16.04.1_amd64.deb
```



