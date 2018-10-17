#!/bin/bash 

set -m 
sudo docker build -t wenhuizhang/tensorforce .
sudo docker run -it --net=host --name=TF  wenhuizhang/tensorforce bash 
