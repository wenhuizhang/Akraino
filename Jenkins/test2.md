# Test for Access Control 

test for access control across different projects

test result, it is a id based DAC, no MAC is enforced

```
#!/bin/bash
set -x
for i in {1..30}; do 
  echo $i; 
  touch 1.txt
  echo $?
  echo $PWD
  cd /root/
  echo $?
  echo $PWD
  cd ..
  echo $?
  cd ./2
  echo $?
  cp 1.txt ../1/
  echo $?
done
exit 0



```
