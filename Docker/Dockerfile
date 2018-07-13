# base image 
FROM ubuntu:14.04

# maintainer
MAINTAINER wenhui<wenhui@gwmail.gwu.edu>

# commands executed in terminal
RUN set -x

RUN touch /etc/apt/apt.conf 
RUN echo "Acquire::http::Proxy "http://135.28.13.11:8080/";" >> /etc/apt/apt.conf 
RUN echo "Acquire::https::Proxy "http://135.28.13.11:8080/";" >> /etc/apt/apt.conf 

RUN export http_proxy=http://one.proxy.att.com:8888
RUN echo $http_proxy
RUN export https_proxy=http://one.proxy.att.com:8888
RUN echo $https_proxy

RUN apt-get update
RUN apt-get install -y git vim  
RUN apt-get install -y openssh-server 
RUN mkdir -p /var/run/ssd



