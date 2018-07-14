#base image 
FROM ubuntu:16.04

# maintainer
MAINTAINER wenhui<wenhui@gwmail.gwu.edu>

# commands executed in terminal
RUN set -x

RUN touch /etc/apt/apt.conf 
RUN echo "Acquire::http::Proxy \"http://135.28.13.11:8080/\";" >> /etc/apt/apt.conf 
RUN echo "Acquire::https::Proxy \"http://135.28.13.11:8080/\";" >> /etc/apt/apt.conf 
# RUN echo  <<EOF>> >> /etc/apt/apt.conf 

RUN export http_proxy=http://one.proxy.att.com:8888
RUN echo $http_proxy
RUN export https_proxy=http://one.proxy.att.com:8888
RUN echo $https_proxy

RUN apt-get update
RUN apt-get install -y git vim  
RUN apt-get install net-tools
RUN apt-get install -y openssh-server 
RUN mkdir -p /var/run/ssd


RUN export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/opt/dell/srvadmin/bin:/opt/dell/srvadmin/sbin



# build deps
RUN apt-get install -y wget tar libnetfilter-queue-dev libnetfilter-queue1 libnfnetlink-dev pkg-config libmagic-dev build-essential libpcre3-dev libpcre3-dbg automake autoconf libtool libpcap-dev libnet1-dev libyaml-dev zlib1g-dev libcap-ng-dev libjansson-dev apache2 


# download source 
# RUN cp /root/suricata/suricata-4.0.4.tar.gz ./

# RUN wget https://www.openinfosecfoundation.org/download/suricata-4.0.4.tar.gz
# RUN cd suricata
# RUN tar -xvf suricata-4.0.4.tar.gz

# configure
# RUN cd suricata-4.0.4
# RUN ./configure --sysconfdir=/etc --localstatedir=/var

# build and install 
# RUN make
# RUN make install
# RUN make install-conf
# RUN make install-rules


# check modes and run 
# RUN ethtool -K eth0 gro off lro off
# RUN /usr/bin/suricata --list-runmodes
# RUN /usr/local/bin/suricata -c /etc/suricata/suricata.yaml -i eth0 --init-errors-fatal
