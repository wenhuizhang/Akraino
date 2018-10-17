# this is a container for running tfcli experiments (also via pycharm) against tensorforce on k8s

# set this to empty string (--build-arg gpu="") if you want to build without GPU
# ARG gpu="-gpu"
ARG gpu=""

FROM tensorflow/tensorflow:latest${gpu}-py3

RUN echo "GPU=$gpu (empty for cpu)"


RUN apt-get update -y
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y --no-install-recommends tzdata python3 python3-dev python3-pip python3-setuptools git dos2unix net-tools iproute2 iputils-ping telnet lsb-release curl vim
RUN apt-get install -y python3-setuptools --upgrade
RUN apt-get install -y build-essential cmake
RUN pip3 install --upgrade pip
RUN pip3 install wheel numpy msgpack msgpack-numpy pydevd dm-sonnet cached_property scipy cython matplotlib pygame msgpack-python pillow virtualenv virtualenvwrapper python-dateutil gym
RUN pip3 install gym[atari]


# install tensorforce manually (to support latest dev branch)
RUN git clone https://github.com/ducandu/tensorforce
WORKDIR tensorforce
RUN git checkout master
RUN git pull
RUN python setup.py install
WORKDIR ../

RUN mkdir /runcontainer
COPY ./example.py /runcontainer/
COPY ./entry.sh /runcontainer/
COPY ./example.py /usr/sbin
COPY ./entry.sh /usr/sbin
WORKDIR /runcontainer

CMD ["set -m"]
CMD ["export PATH=$PATH:/runcontainer/"]
CMD ["echo $PATH"]
RUN chmod +x entry.sh
RUN chmod +x example.py
# CMD ["/runcontainer/entry.sh"]
#ENTRYPOINT ["entry.sh"]
#CMD [""]
 CMD ["bash"]
#CMD ["python exmaple.py"]
