#!/bin/bash

# check if file exists, if not print error message
if [[ ! -f $1 ]]
then
    1>&2 echo "THIS IS AN ERROR MESSAGE TO STDERR"
    exit 1
else
    # if file exists, print 3rd line
    head -n 3 $1 | tail -n 1
fi
