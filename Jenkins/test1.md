# Test 1 for Exit

1. test 1

```
#!/bin/bash
for i in {1..30}; do 
  echo $i; 
  sleep 1; 
done

```


2. test 2

```
#!/bin/bash
for i in {1..30}; do 
  echo $i; 
  sleep 1; 
done
exit 1
```


3. test 3

```
#!/bin/bash
for i in {1..30}; do 
  echo $i; 
  sleep 1; 
done
exit 0
```

4. test 4

```
#!/bin/bash
for i in {1..30}; do 
  echo $i; 
  sleep 1; 
done
exit 2
```
