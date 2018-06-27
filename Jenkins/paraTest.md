# Project Parameter 


General --> Add parameters 




```
#!/bin/bash
echo "VERSION NUMBER: $VERSION_NUMBER"
echo "ENVIRONMENT:    $ENVIRONMENT"
echo "RUN_TESTS:      $RUN_TESTS"
echo
if [ "$RUN_TESTS" = "true" ];
then
    echo "Running Tests!";
else
    echo "Not Testing!";
fi
```
