#/bin/bash 
set -m 

sudo docker kill $(sudo docker ps -q)
sudo docker rm $(sudo docker ps -a -q)
sudo docker rmi $(sudo docker images -q) --force 
sudo docker volume ls -qf dangling=true | xargs -r sudo docker volume rm
